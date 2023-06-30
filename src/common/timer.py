import time
from contextlib import contextmanager
from typing import Dict, Optional


@contextmanager
def timer(prefix='', *, count: int = None, unit: str = None, stats: Dict[str, any] = None, minimum: Optional[float] = None, show: bool = True):
    started = time.time()
    yield
    duration = time.time() - started

    frequency = None
    frequency_text = ''
    if count and isinstance(count, int):
        frequency = count / max(1e-6, duration)
        frequency_text = f' ({frequency:.1f}{" " + unit if unit else ""}/s)'

    if stats is not None:
        stats['duration'] = duration
        if count is not None:
            stats['count'] = count
        if unit is not None:
            stats['unit'] = unit
        if frequency is not None:
            stats['frequency'] = frequency

    if minimum is None or duration >= minimum:
        print(f'{prefix} in {duration:.3f}s{frequency_text}')
