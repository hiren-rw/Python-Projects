"""Simple text-file operations used by the toolkit."""


def create_file(filename):
    """Create an empty file without replacing an existing one."""
    with open(filename, "x", encoding="utf-8"):
        pass


def write_file(filename, text):
    """Write text, replacing any existing contents."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)


def read_file(filename):
    """Read and return the complete text of a file."""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def append_file(filename, text):
    """Add text to the end of a file (or create it if missing)."""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
