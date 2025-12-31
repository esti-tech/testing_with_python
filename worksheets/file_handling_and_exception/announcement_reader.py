import os


def read_announcement(path: str | None = None) -> str:
    """Read and print the announcement file.

    If `path` is None, this function will look for `announcement.txt`
    located in the same folder as this script.

    Returns the file contents as a string.
    """
    if path is None:
        base = os.path.dirname(__file__)
        path = os.path.join(base, "announcement.txt")

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    print(text)
    return text


if __name__ == "__main__":
    read_announcement()
