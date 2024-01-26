#!/usr/bin/python3
import hidden_4

# This function prints all the names defined by the compiled module hidden_4.pyc
# excluding those starting with '__'.
def print_names():
    names = dir(hidden_4)
    filtered_names = [name for name in names if not name.startswith('__')]
    for name in sorted(filtered_names):
        print("{}".format(name))


if __name__ == "__main__":
    # Prints all the names defined by the compiled module hidden_4.pyc
    print_names()
