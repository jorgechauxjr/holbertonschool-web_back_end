#!/usr/bin/env python3
"""
measures the total execution time for wait_n(n, max_delay)
"""
import asyncio
from typing import List
wait_n = __import__('1-concurrent_coroutines.py').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """returns total_time / n"""
    initial_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()
    return (end_time - initial_time) / n
