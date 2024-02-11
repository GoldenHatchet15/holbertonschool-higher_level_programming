#!/usr/bin/python3
"""
This module extends the functionality of previous tasks to implement a script
that dynamically adds command-line arguments to a persistent list stored in
a JSON file ("add_item.json").

Utilizing the previously defined functions 'save_to_json_file' and
'load_from_json_file' from modules 'save_to_json_file' and
'load_from_json_file' respectively, it reads the existing list from the file,
appends the new items (arguments given to the script), and saves the updated
list back into the same JSON file.

If "add_item.json" does not exist, it will be created on the first run. This
approach provides a simple way to accumulate data over time from script
executions without losing the previous state.
"""

import sys
# Import the necessary functions from their respective modules.
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# The JSON file where the list will be stored and updated.
filename = "add_item.json"

try:
    # Attempt to load the existing data from the JSON file.
    items = load_from_json_file(filename)
except FileNotFoundError:
    # If the file doesn't exist, start with an empty list.
    items = []

# Extend the current list with command-line arguments (excluding the script name).
items.extend(sys.argv[1:])

# Save the updated list back to the JSON file, preserving the additions.
save_to_json_file(items, filename)
