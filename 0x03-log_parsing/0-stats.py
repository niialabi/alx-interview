#!/usr/bin/python3
import sys

# Initialize metrics
file_size = 0
status_codes = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0


def print_output():
    """ func prints specified output """
    print("File size:", file_size)
    for key, value in status_codes.items():
        if value:
            print("{}: {}".format(key, value))


try:
    for line in sys.stdin:
        line_count += 1
        line = line.split()
        try:
            file_size = int(line[-1])
            file_size += file_size
        except (IndexError, ValueError, TypeError):
            continue
        try:
            status_code = int(line[-2])
            if status_code in status_codes.keys():
                status_codes[status_code] += 1
        except (IndexError, ValueError, TypeError):
            continue
        if line_count == 10:
            print_output()
            line_count = 0
    print_output()
except KeyboardInterrupt:
    print_output()
