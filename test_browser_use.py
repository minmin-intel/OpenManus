import asyncio

from app.agent.browser import BrowserAgent
from app.logger import logger


async def main():
    agent = BrowserAgent()
    task = "In the Scikit-Learn July 2017 changelog, what other predictor base command received a bug fix? Just give the name, not a path."
    task = "The photograph in the Whitney Museum of American Art's collection with accession number 2022.128 shows a person holding a book. Which military unit did the author of this book join in 1813? Answer without using articles."
    task = "Weather in San Francisco March 1, 2025"
    await agent.run(task)


if __name__ == "__main__":
    asyncio.run(main())