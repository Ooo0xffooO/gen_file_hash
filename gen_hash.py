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
    parser.add_argument("-m", dest="mode", choices=["md5", "sha1", "sha256"], help="hash mode")
    args = parser.parse_args()

    if args.mode == "md5":
        md5hasher = hashlib.md5(read_file(args.file_path))
        print(md5hasher.hexdigest())
    elif args.mode == "sha1":
        sha1hasher = hashlib.sha1(read_file(args.file_path))
        print(sha1hasher.hexdigest())
    elif args.mode == "sha256":
        sha256hasher = hashlib.sha256(read_file(args.file_path))
        print(sha256hasher.hexdigest())
