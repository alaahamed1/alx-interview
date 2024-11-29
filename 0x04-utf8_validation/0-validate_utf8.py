#!/usr/bin/python3
"""UTF-8 Validation module"""


def is_char(byte):
    """Check if the integer as a byte represent a character
    """
    if byte & 128 == 0:
        return True
    return False


def is_continuation(byte):
    """Check if the byte is a continuation byte
    the 8 least significant bits equals 10xxxxxx
    """
    if byte & 128 == 128:
        if byte & 64 == 0:
            return True
    return False


def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding. """
    n_ones = -1
    for byte in data:
        if is_continuation(byte):
            if n_ones > 0:
                n_ones -= 1
                continue
            return False
        if n_ones > 0:
            return False
        if is_char(byte):
            continue
        n_ones = -1
        x = 128
        while x & byte == x:
            x = x >> 1
            n_ones += 1
            if n_ones >= 4:
                return False
    if n_ones > 0:
        return False
    return True
