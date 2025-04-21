import asyncio
from schedule import schedule_daily_work
from tasks.runner import run_all_tasks
from utils.notifier import send_discord_notification

async def main():
    await send_discord_notification("🤖 Bot iniciado y ejecutándose 16h hoy!")
    await schedule_daily_work(run_all_tasks)

if __name__ == '__main__':
    asyncio.run(main())
