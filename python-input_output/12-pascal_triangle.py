#!/usr/bin/python3
"""
12-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns list of lists of integers representing Pascal's triangle of n
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # first element of each row is always 1
        if i > 0:
            for j in range(1, i):  # elements between first and last
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)  # last element of each row is always 1
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    n = 5
    triangle = pascal_triangle(n)
    for row in triangle:
        print(row)
