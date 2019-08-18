"""
    using asyncio and await, but still syncronous as using a blocking function
"""
from datetime import datetime
import asyncio

# since very_long_routine is awaited in main(), it has to be an async function
async def very_long_routine(index):
    print(f"    start: {index}")
    # note that time.sleep() is a blocking function. Prevents await from working
    # replacing time.sleep() with non blocking asyncio.sleep()
    await asyncio.sleep(5)
    print(f"    end:   {index}")


# since main is invoked by asyncio.run(), it has to be an async function
async def main():
    program_start_time = datetime.utcnow()
    print(f"started at {program_start_time}")

    # changing the invocation loop to list comprehension inside the gather method.
    await asyncio.gather(*(very_long_routine(i) for i in range(1, 6)))
    # note that now all the fuctions are starting at the same time.
    # note also that the logic is now slightly different, as I had to remove prints around function calls.

    program_end_time = datetime.utcnow()
    print(f"ended   at {program_end_time}")
    print(f"total duration: {(program_end_time - program_start_time).total_seconds()}")


if __name__ == "__main__":
    # replace simple invocation with asyncio.run() invocation
    asyncio.run(main())
