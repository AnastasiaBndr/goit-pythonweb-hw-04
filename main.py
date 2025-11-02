import argparse
from asyncFunctions.read_folder import read_folder
import asyncio
import logging

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

async def main():
    parser = argparse.ArgumentParser(description="Process a folders path:")
    parser.add_argument('source_folder', type=str,
                        help="Path to source folder")
    parser.add_argument('--output_folder', type=str,
                        help="Path to output folder")

    args = parser.parse_args()

    await read_folder(args.source_folder, args.output_folder)



if __name__ == '__main__':
   asyncio.run(main())
