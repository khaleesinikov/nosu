import os
from os.path import exists, isdir
from typing import List


def to_gigs(size: int):
    return round(size / 1024 ** 3, 2)


def remove_files(path: str, extensions: List[str]):
    file_count, size_count = 0, 0

    for folder in os.scandir(path):
        if not folder.is_dir():
            continue  # avoids stray files in songs folder

        for file in os.scandir(folder.path):
            if not file.is_file():
                continue  # avoids further subfolders

            for ext in extensions:
                if file.name.endswith("." + ext):
                    size = os.stat(file.path).st_size
                    try:
                        os.remove(file.path)
                        file_count += 1
                        size_count += size
                    except PermissionError:
                        print(f"Failed to remove {file.name}")

    print(f"Removed {str(file_count)} files, saving {str(to_gigs(size_count))}GB of space.")


def main():
    path = input("Path to osu! songs folder: ")
    extensions = input("File extensions to remove: ").split(" ")

    if exists(path):
        if isdir(path):
            remove_files(path, extensions)
        else:
            print("Path is not a valid directory.")
    else:
        print("Path does not exist.")


main()
