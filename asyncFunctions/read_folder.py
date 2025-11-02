import aiofiles
import asyncio
import os
import logging
from .copy_file import copy_file

logger = logging.getLogger(__name__)

async def read_file_async(filepath):
    try:
        async with aiofiles.open(filepath, mode='rb') as f:
            return await f.read()
    except Exception as e:
        logger.error(f"Error reading {filepath}: {e}")
        return None


async def read_folder(source_path, output_path):
    contents = []
    if not os.path.isdir(source_path):
        logger.error(f"Folder {source_path} does not exist!")
        return

    async def read_folder_recursively(source_path):
        for item_name in os.listdir(source_path):
            item_path = os.path.join(source_path, item_name)

            if os.path.isfile(item_path):
                contents.append(item_path)
            elif os.path.isdir(item_path):
                await read_folder_recursively(item_path)

    await read_folder_recursively(source_path)

    tasks = [read_file_async(filepath) for filepath in contents]
    file_data = await asyncio.gather(*tasks)

    all_data = [

        {"path": path, "content": data}
        for path, data in zip(contents, file_data)
        if data is not None

    ]

    await copy_file(output_path, all_data)
