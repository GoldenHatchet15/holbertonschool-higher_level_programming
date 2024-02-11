#!/usr/bin/python3

def read_file(filename=""):
    """Reads a text file (UTF-8) and prints it to stdout."""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')

# This block below is for testing
# You can use it to test the function
if __name__ == "__main__":
    read_file("my_file_0.txt")
