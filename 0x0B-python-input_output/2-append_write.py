def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8).

    Args:
        filename (str): The name of the file.
        text (str): The text to append.

    Returns:
        int: The total number of characters written.
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)
    return len(text)
