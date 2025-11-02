import os
import asyncio
import shutil
import logging

logger = logging.getLogger(__name__)

async def copy_file(output_path, files):
    
    if not os.path.isdir(output_path):
        logger.error(f"Folder {output_path} does not exist!")
        return
    
    async def copy_one_file(file):

        filepath = file["path"]

        _, extension = os.path.splitext(filepath)

        extension_directory_path = os.path.join(output_path, extension[1:])

        await asyncio.to_thread(os.makedirs,extension_directory_path,exist_ok=True)
        await asyncio.to_thread(shutil.copy2,filepath,extension_directory_path)

    tasks = [copy_one_file(file) for file in files]
    await asyncio.gather(*tasks)
