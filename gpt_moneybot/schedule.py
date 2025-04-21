import asyncio
from datetime import datetime, timedelta
import random

async def schedule_daily_work(task_callback):
    start_time = datetime.now()
    total_runtime = timedelta(hours=16)
    end_time = start_time + total_runtime

    while datetime.now() < end_time:
        await task_callback()
        wait_time = random.randint(300, 900)
        await asyncio.sleep(wait_time)
