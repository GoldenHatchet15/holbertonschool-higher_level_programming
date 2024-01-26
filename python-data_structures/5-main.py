#!/usr/bin/python3
no_c = __import__('5-no_c').no_c
if __name__ == "__main__":
    # function that removes all characters c and C from a string.
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
