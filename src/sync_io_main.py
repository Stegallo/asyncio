"""
"""
import time
from datetime import datetime
import asyncio


async def very_long_routine(index):
    print(f"    start: {index}")
    time.sleep(5)
    print(f"    end:   {index}")


async def main():
    program_start_time = datetime.utcnow()
    print(f"started at {program_start_time}")
    for i in range(1, 6):
        print(f"    iteration {i} started at {datetime.utcnow()}")
        await very_long_routine(i)
        print(f"    iteration {i} ended   at {datetime.utcnow()}")
    program_end_time = datetime.utcnow()
    print(f"ended   at {program_end_time}")
    print(f"total duration: {(program_end_time - program_start_time).total_seconds()}")


if __name__ == "__main__":
    LOOP = asyncio.get_event_loop()
    LOOP.run_until_complete(main())
    LOOP.close()
