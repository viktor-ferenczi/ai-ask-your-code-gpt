import os
import shutil
import sys


def enable_core_dumps():
    if sys.platform != 'linux':
        return

    for path in ('/', '/home', '/var'):
        if shutil.disk_usage(path).free < 500_000_000_000:
            return

    import resource
    import signal

    resource.setrlimit(resource.RLIMIT_CORE, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))
    signal.signal(signal.SIGQUIT, lambda signum, frame: os.abort())

    print('Core dumps enabled')
