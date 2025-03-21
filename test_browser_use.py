import asyncio

from app.agent.browser import BrowserAgent
from app.logger import logger


async def main():
    agent = BrowserAgent()
    # try:
    #     prompt = input("Enter your prompt: ")
    #     if not prompt.strip():
    #         logger.warning("Empty prompt provided.")
    #         return

    #     logger.warning("Processing your request...")
    #     await agent.run(prompt)
    #     logger.info("Request processing completed.")
    # except KeyboardInterrupt:
    #     logger.warning("Operation interrupted.")
    prompt = "What fruits are in the 2008 painting Embroidery from Uzbekistan"
    prompt = "Weather tomorrow in San Francisco"
    await agent.run(prompt)


if __name__ == "__main__":
    asyncio.run(main())