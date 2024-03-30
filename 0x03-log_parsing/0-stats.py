#!/usr/bin/python3
import sys

# Initialize metrics
file_size = 0
status_codes = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0

try:
    # Read from stdin line by line
    for line in sys.stdin:
        line_count += 1

        # Parse line
        try:
            ip, date, request, status_code, size = line.split(" - [")[0], \
                line.split(" - [")[1].split("]")[0], line.split('\"')[1], \
                int(line.split('\"')[2].split(" ")[1]), \
                int(line.split('\"')[2].split(" ")[2])
        except (IndexError, ValueError):
            continue  # Skip if line format is incorrect

        # Update metrics
        file_size += size
        status_codes[status_code] += 1

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print(f"File size: {file_size}")
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")


            # Reset metrics
            file_size = 0
            status_codes = {
                200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
            }

except KeyboardInterrupt:
    # Print metrics on keyboard interruption
    print(f"\nFile size: {file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")
