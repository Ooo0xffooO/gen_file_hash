import hashlib
import argparse
from pathlib import Path
from typing import Optional, Union


def read_file(file: Optional[Union[Path, str]]) -> bytes:
    if not isinstance(file, Path):
        file = Path(file)
    if not file.exists():
        raise ValueError("this file not exits")
    with open(file=file, mode='rb') as f:
        content = f.read()
    return content


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="file path")
    args = parser.parse_args()

    md5hasher = hashlib.md5(read_file(args.file_path))
    print(md5hasher.hexdigest())
