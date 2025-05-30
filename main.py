import asyncio

from app.agent.manus import Manus
from app.logger import logger


async def main():
    # Create and initialize Manus agent
    agent = await Manus.create(max_steps=15)
    try:
        # prompt = input("Enter your prompt: ")
        # if not prompt.strip():
        #     logger.warning("Empty prompt provided.")
        #     return

        # logger.warning("Processing your request...")
        prompt = """Nagivate to http://localhost:9083/admin and login with the credentials:
        username: admin
        password: admin1234
        Then, find out What are the top-3 best-selling product in **Jan 2023**? Today is May 2025.
"""
        await agent.run(prompt)
        logger.info("Request processing completed.")
    except KeyboardInterrupt:
        logger.warning("Operation interrupted.")
    finally:
        # Ensure agent resources are cleaned up before exiting
        await agent.cleanup()


if __name__ == "__main__":
    asyncio.run(main())
