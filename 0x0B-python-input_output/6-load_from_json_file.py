#!/usr/bin/python3
"""Describes a JSON file-reading function."""
import json


def load_from_json(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
