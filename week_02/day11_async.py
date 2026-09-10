import asyncio

async def say_hello():
    print("Hello")

async def main():
    await say_hello()

asyncio.run(say_hello())