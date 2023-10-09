#!/usr/bin/env python3
"""imported wait_random from the previous python file"""

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns list of all delays in ascending order"""
    tasks = [wait_random(max_delay) for i in range(n)]
    completed_tasks = await asyncio.gather(*tasks)

    sorted_delays = sorted(completed_tasks)

    return sorted_delays
