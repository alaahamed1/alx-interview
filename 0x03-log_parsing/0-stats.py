#!/usr/bin/python3
"""This module processes log entries from a stream
and calculates the total file size and the count of status codes.
"""
import signal
import sys
import re

# Regex pattern
pattern = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s-\s'  # IP address
    r'\[(?P<date>[^\]]+)\]\s'                # Date
    r'"GET\s/projects/260\sHTTP/1.1"\s'      # Request line
    r'(?P<status>\d{3})\s'                   # Status code
    r'(?P<size>\d+)',                        # File size
    re.VERBOSE
)

def handler(segnum, frame):
    """Prints the total file size and the count of status codes."""
    print(f"File size: {total_size}")
    for k, v in sorted(status_code_d.items()):
        print(f"{k}: {v}")
    sys.exit(0)

signal.signal(signal.SIGINT, handler)

total_size = 0
status_code_d = dict()
line_nums = 0


for line in sys.stdin:
    the_match = pattern.match(line)
    if the_match is False:
        continue
    total_size += int(the_match.group('size'))
    if the_match.group('status') in status_code_d:
        status_code_d[the_match.group('status')] += 1
    else:
        status_code_d[the_match.group('status')] = 1
    line_nums += 1

    if line_nums >= 10:
        print(f"File size: {total_size}")
        for k, v in sorted(status_code_d.items()):
            print(f"{k}: {v}")
        line_nums = 0
