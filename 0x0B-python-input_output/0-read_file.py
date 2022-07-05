#!/usr/bin/python3
"""Describe a text file function"""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout"""
    with ope(filename, encoding="utf-8") as f:
        print(f.read(), end="")
