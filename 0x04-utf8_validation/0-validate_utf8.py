#!/usr/bin/python3
""" Module for the function `is_valid_utf8` """

from typing import List


def validUTF8(data: List[int]) -> bool:
    """ Return: True if data is a valid UTF-8 encoding, else return False """
    exp_cont_bytes = 0

    for byte in data:
        binary_representation = f"{byte:08b}"[-8:]

        if binary_representation.startswith("0") and exp_cont_bytes == 0:
            continue

        if binary_representation.startswith("110") and exp_cont_bytes == 0:
            exp_cont_bytes = 1
            continue

        if binary_representation.startswith("1110") and exp_cont_bytes == 0:
            exp_cont_bytes = 2
            continue

        if binary_representation.startswith("11110") and exp_cont_bytes == 0:
            exp_cont_bytes = 3
            continue

        if binary_representation.startswith("10") and exp_cont_bytes > 0:
            exp_cont_bytes -= 1
            continue

        return False

    return exp_cont_bytes == 0
