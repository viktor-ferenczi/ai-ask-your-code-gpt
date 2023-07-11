#!/usr/bin/env python3
import argparse
import gzip
import os
import os.path
import shutil
import signal
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import requests
import yaml

HOME_DIR = Path.home()  # Home directory for the user
LOG_DIR = HOME_DIR / 'log'  # Directory for logs
OLD_LOG_DIR = LOG_DIR / 'old'  # Directory for logs
PID_DIR = HOME_DIR / 'pid'  # Directory for pid files
SRC_DIR = HOME_DIR / 'src'  # Directory for sources
BIN_DIR = HOME_DIR / 'bin'  # Directory for scripts
CONFIG_FILE = BIN_DIR / 'services.yaml'  # Configuration file for services
MAX_LOG_FILE_SIZE = 20_000_000  # Rotate log files after reaching this size


class Manager:
    def __init__(self, ignore_pid_files=False):
        self.services = self.load_services()
        self.ignore_pid_files = ignore_pid_files

    def log(self, message):
        print(f"{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}: {message}", file=sys.stderr)

    def load_services(self):
        with open(CONFIG_FILE, 'r') as f:
            return yaml.safe_load(f)

    def status(self, service, instance):
        status = 'Missing'
        if self.is_running(service, instance):
            status = 'Frozen'
            if self.is_healthy(service, instance):
                status = 'Running'

        print(f"{status}: {service['name']}-{instance:02d}")

    def start(self, service, instance):
        if self.is_running(service, instance):
            print(f"Already running: {service['name']}-{instance:02d}")
            return

        self.rotate_logs(service, instance)

        name = service['name']
        command = [os.path.expanduser(v) for v in service['command']]
        work_dir = os.path.expanduser(service['work_dir'])
        port = service['base_port'] + instance

        environment = {
            'ENVIRONMENT': os.environ['ENVIRONMENT'],
            'HTTP_PORT': str(port),
            'PYTHONPYCACHEPREFIX': str(HOME_DIR / '.cache' / 'python'),
            'PYTHONUNBUFFERED': '1',
            'PYTHONPATH': str(SRC_DIR),
        }

        log_file = LOG_DIR / f"{name}-{instance:02d}.log"
        pid_file = PID_DIR / f"{name}-{instance:02d}.pid"

        with open(log_file, "a") as out, open(pid_file, "w") as pidf:
            proc = subprocess.Popen(['/usr/bin/nohup'] + command, cwd=work_dir, env=environment, stdout=out, stderr=out, stdin=None)
            pidf.write(str(proc.pid))

        print(f"Started: {name}-{instance:02d} with PID {proc.pid} on port {port}")

    def stop(self, service, instance):
        pid_file = PID_DIR / f"{service['name']}-{instance:02d}.pid"

        if not self.is_running(service, instance):
            print(f"Not running: {service['name']}-{instance:02d}")

            if os.path.exists(pid_file):
                os.remove(pid_file)

            return

        with open(pid_file, 'r') as f:
            pid = int(f.read().strip())

        os.kill(pid, signal.SIGTERM)
        print(f"Stopped: {service['name']}-{instance:02d} with PID {pid}")

        os.remove(pid_file)

    def restart(self, service, instance):
        self.stop(service, instance)
        self.start(service, instance)

    def check_pid_exists(self, pid: int) -> bool:
        """Check whether pid exists in the current process table."""
        try:
            os.kill(pid, signal.SIG_DFL)
        except ProcessLookupError:
            return False
        except PermissionError:
            return True
        return True

    def is_running(self, service, instance):
        pid_file = PID_DIR / f"{service['name']}-{instance:02d}.pid"
        if not pid_file.exists():
            return False

        with open(pid_file, 'r') as f:
            try:
                pid = int(f.read().strip())
            except ValueError:
                return False

        return self.check_pid_exists(pid)

    def is_healthy(self, service, instance):
        try:
            response = requests.get(f"http://127.0.0.1:{service['base_port'] + instance}", timeout=30.0)
        except requests.RequestException:
            response = None
        return response is not None and response.status_code == 200

    def keepalive(self, service, instance):
        if not self.is_running(service, instance):
            self.log(f"Missing: {service['name']}-{instance:02d}")
            self.start(service, instance)
            return

        if not self.is_healthy(service, instance):
            self.log(f"Frozen: {service['name']}-{instance:02d}")
            self.restart(service, instance)
            return

        self.log(f"Good: {service['name']}-{instance:02d} process")

    def rotate_logs(self, service, instance):
        basename = f"{service['name']}-{instance:02d}"
        path = LOG_DIR / f'{basename}.log'

        if not os.path.exists(path):
            return

        if os.path.getsize(path) < MAX_LOG_FILE_SIZE:
            return

        if path.is_file():
            OLD_LOG_DIR.mkdir(parents=True, exist_ok=True)
            ts = datetime.utcnow().strftime('%Y%m%d-%H%M%S')
            gz_path = str(OLD_LOG_DIR / f'{basename}.{ts}.log.gz')
            with open(path, 'rb') as f_in, gzip.open(gz_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
            os.remove(path)

    def handle_service(self, service, action):
        for instance in range(service['instances']):
            if action == 'status':
                self.status(service, instance)
            elif action == 'start':
                self.start(service, instance)
            elif action == 'stop':
                self.stop(service, instance)
            elif action == 'restart':
                self.restart(service, instance)
            elif action == 'keepalive':
                self.keepalive(service, instance)
            else:
                print(f"Unknown action: {action}")
                sys.exit(1)

    def handle(self, action, service_names=None):
        for service in self.services:
            if not service_names or service['name'] in service_names:
                self.handle_service(service, action)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ignore-pid-files", action='store_true', help="Ignore existing PID files (useful after OS boot)")
    parser.add_argument("action", help="status, start, stop, restart, keepalive")
    parser.add_argument("service_names", nargs='*', default=None, help="Names of the services to manage (all services if not specified)")
    args = parser.parse_args()

    PID_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    OLD_LOG_DIR.mkdir(parents=True, exist_ok=True)

    manager = Manager(args.ignore_pid_files)
    manager.handle(args.action, args.service_names)


if __name__ == "__main__":
    main()
