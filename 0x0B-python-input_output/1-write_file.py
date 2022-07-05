#!/usr/bin/python3
"""Describe a file function"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file

    Args:
        filename (str): The name of the file to write
        text (str): the text to write to the file
    Returns:
        The number of character written """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
