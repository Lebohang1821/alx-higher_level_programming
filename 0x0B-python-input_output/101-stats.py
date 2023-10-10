#!/usr/bin/python3
"""
This script reads from standard input and computes metrics for log data.

After every ten lines or when a keyboard interruption (CTRL + C) occurs,
it prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

def print_stats(size, status_codes):
    """
    Print accumulated metrics.

    Args:
        size (int): The accumulated file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("Total file size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_stats(size, status_codes)
                line_count = 1
            else:
                line_count += 1

            line_parts = line.split()

            try:
                size += int(line_parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line_parts[-2] in valid_codes:
                    if status_codes.get(line_parts[-2], -1) == -1:
                        status_codes[line_parts[-2]] = 1
                    else:
                        status_codes[line_parts[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
