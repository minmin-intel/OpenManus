import asyncio

from app.agent.browser import BrowserAgent
from app.agent.manus import Manus
from app.logger import logger

import pandas as pd
import os
import argparse
from datetime import datetime

def parse_args():
    parser = argparse.ArgumentParser(description="Test Browser Agent")
    parser.add_argument(
        "--quick_test",
        action="store_true",
        help="Run a quick test with a single question.",
    )
    parser.add_argument(
        "--input",
        type=str,
        help="Path to the input CSV or JSONL file containing questions.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="test_results.jsonl",
        help="Path to the output JSONL file for storing test results.",
    )
    return parser.parse_args()

def get_test_data(args):
    if args.input is not None:
        if args.input.endswith(".csv"):
            df = pd.read_csv(args.input)
        elif args.input.endswith(".jsonl"):
            df = pd.read_json(args.input, lines=True)
        else:
            raise ValueError("Unsupported file format. Please provide a CSV or JSONL file.")
        
        if os.path.exists(args.output):
            tested = pd.read_json(args.output, lines=True)
            df = df[~df["Question"].isin(tested["question"])]
        print(f"Loaded {len(df)} questions from {args.input}")
        return df
    else:
        raise ValueError("No input file provided. Please specify a CSV or JSONL file.")

def append_to_output_file(output_file, data):
    import json
    with open(output_file, "a") as f:
        f.write(json.dumps(data) + "\n")

def save_as_csv(answers_file):
    df = pd.read_json(answers_file, lines=True)
    df.to_csv(answers_file.replace(".jsonl", ".csv"), index=False)
    print(f"Saved answers to {answers_file.replace('.jsonl', '.csv')}")

async def main():
    args = parse_args()
    
    # Initialize the Manus agent
    agent = Manus()
    # agent = BrowserAgent()

    if args.quick_test:
        task = "Who nominated the only Featured Article on English Wikipedia about a dinosaur that was promoted in November 2016?"
        # task = "Weather in San Francisco March 1, 2025"
        response = await agent.run(task)
        print(f"Response: {response}")
    else:
        df = get_test_data(args)
        df = df.head(1)
        for i, row in df.iterrows():
            question = row["Question"]
            print(f"Processing question {i}: {question}")

            start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            response = await agent.run(question)
            end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Response: {response}")

            data = {
                "question": question,
                "prediction": response,
                "true_answer": row["Final answer"],
                "task": row["Level"],
                "start_time": start_time,
                "end_time": end_time,
            }
            # Append the result to the output file
            append_to_output_file(args.output, data)
            print("="*50)
                
        



if __name__ == "__main__":
    args = parse_args()
    asyncio.run(main())
    save_as_csv(args.output)