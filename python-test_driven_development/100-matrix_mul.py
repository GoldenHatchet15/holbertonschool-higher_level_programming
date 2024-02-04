#!/usr/bin/python3
"""
This module provides a function to multiply two matrices.
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a: The first matrix, a list of lists of integers/floats.
        m_b: The second matrix, also a list of lists of integers/floats.

    Raises:
        TypeError: If m_a or m_b is not a list of lists, or if they contain
        non-numbers.
        ValueError: If m_a or m_b is empty, or if they cannot be multiplied.

    Returns:
        A new matrix representing the product of m_a by m_b.
    """
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]] or m_b == [] or m_b == [[]]:
        raise ValueError(
            "m_a can't be empty" if not m_a or m_a == [[]] else "m_b can't be empty"
        )
    if not all(isinstance(el, (int, float)) for row in m_a for el in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(el, (int, float)) for row in m_b for el in row):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            sum_product = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row_result.append(sum_product)
        result.append(row_result)
    return result
