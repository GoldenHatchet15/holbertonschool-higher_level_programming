#!/usr/bin/python3
import sys

# Save_to_json_fileand load_from_json_file are defined in the following modules
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Add all arguments except the first one (script name) to the list
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
