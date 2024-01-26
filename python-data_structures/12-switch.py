#!/usr/bin/python3
if __name__ == "__main__":
    a = 89
    b = 10
    a, b = b, a  # Swapping the values of a and b
    print("a={:d} - b={:d}".format(a, b))
