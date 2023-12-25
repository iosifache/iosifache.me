import sys
from pathlib import Path
from datetime import datetime
import re

METADATA = """---
title: Open source projects
date: {}
slug: oss
status: hidden
---

"""


def main():
    if len(sys.argv) != 3:
        exit(1)

    readme_path = Path(sys.argv[1])
    page_path = Path(sys.argv[2])
    if not readme_path.exists():
        exit(1)

    content = read_file(readme_path)
    new_content = convert_profile_readme(content)
    write_file(page_path, new_content)


def read_file(path: Path) -> str:
    with path.open(mode="r") as file:
        return file.read()


def convert_profile_readme(readme_content: str) -> str:
    date = get_date()

    readme_content = re.sub(
        r"### (.*)",
        r"# \1",
        readme_content,
    )
    readme_content = re.sub(
        r"    <summary>(.*)</summary>",
        r"\1",
        readme_content,
    )
    readme_content = re.sub(
        "This document was automatically generated",
        "This page was automatically generated",
        readme_content,
    )

    new_lines = [
        line
        for line in readme_content.split("\n")
        if line != "<details>" and line != "</details>"
    ]
    readme_content = "\n".join(new_lines)

    return METADATA.format(date) + readme_content


def get_date() -> str:
    now = datetime.now()

    return now.strftime("%Y-%m-%d %H:%M")


def write_file(path: Path, readme_content: str) -> None:
    with path.open(mode="w") as file:
        file.write(readme_content)


if __name__ == "__main__":
    main()
