import os
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from threading import Lock

print_lock = Lock()


def ensure_directory_exists(path):
    os.makedirs(path, exist_ok=True)


def copy_file(src_file, dest_dir):
    extension = src_file.suffix.lstrip('.').lower()
    target_dir = dest_dir / extension
    ensure_directory_exists(target_dir)
    shutil.copy2(src_file, target_dir / src_file.name)


def process_directory(src_dir, dest_dir, executor):
    for item in src_dir.iterdir():
        if item.is_dir():
            executor.submit(process_directory, item, dest_dir, executor)
        elif item.is_file():
            executor.submit(copy_file, item, dest_dir)


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <source_directory> [<destination_directory>]")
        return

    src_path = Path(sys.argv[1])
    dest_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('dist')

    if not src_path.is_dir():
        print(f"Source directory '{src_path}' does not exist.")
        return

    ensure_directory_exists(dest_path)

    with ThreadPoolExecutor() as executor:
        process_directory(src_path, dest_path, executor)

    print(f"Files have been sorted and copied to '{dest_path}'")


if __name__ == "__main__":
    main()
