#!/usr/bin/python3#!/usr/bin/python3
""" Mod for the func rotate_2d_matrix """


def rotate_2d_matrix(matrix):
    """Rotate an n x n 2D matrix 90 degrees clockwise"""
    matrix[:] = [list(row) for row in zip(*matrix[::-1])]
