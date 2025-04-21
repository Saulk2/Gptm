import asyncio
from tasks.clickworker import run_clickworker
from tasks.mturk import run_mturk
from tasks.remotasks import run_remotasks

async def run_all_tasks():
    await run_clickworker()
    await run_mturk()
    await run_remotasks()
