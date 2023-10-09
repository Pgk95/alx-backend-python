#!/usr/bin/env python3
"""imported wait_random from the previous python file"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> float:
    """"returns the list of all the delays (float values)."""
    listed_delays = []
    for i in range(n):
        listed_delays.append(await wait_random(max_delay))
        return sorted(listed_delays)
