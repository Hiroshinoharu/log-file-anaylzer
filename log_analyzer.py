"""
File: log_analyzer.py
Author: Max Ceban
Date: 2025-04-08
Description: This script analyzes a log file and generates a summary of the requests.
"""
import re
from collections import defaultdict, Counter
from pathlib import Path

LOG_PATTERN = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+).*?\[(?P<datetime>[^\]]+)\] '
    r'"(?P<method>GET|POST|PUT|DELETE|HEAD) (?P<path>[^ ]+) HTTP/1\.[01]" '
    r'(?P<status>\d{3})'
)

def parse_log(file_path):
    counters = {
        'ips': Counter(),
        'statuses': Counter(),
        'urls': Counter(),
    }

    with open(file_path, 'r') as f:
        for line in f:
            match = LOG_PATTERN.match(line)
            if not match:
                continue

            data = match.groupdict()
            counters['ips'][data['ip']] += 1
            counters['statuses'][data['status']] += 1
            counters['urls'][data['path']] += 1

    return counters

def print_summary(counters):
    print('Summary of the requests:')
    print('------------------------')
    print('Most common IPs:')
    for ip, count in counters['ips'].most_common(5):
        print(f'{ip}: {count} requests')
    
    print('\nMost common statuses:')
    for status, count in counters['statuses'].most_common(5):
        print(f'{status}: {count} requests')

    print('\nMost common URLs:')
    for url, count in counters['urls'].most_common(5):
        print(f'{url}: {count} requests')
    print('------------------------')
    print('End of summary')
    print('------------------------')

def main():
    log_file = input('Enter the path to the log file: ').strip()
    if not Path(log_file).is_file():
        print(f'File {log_file} does not exist.')
        return

    counters = parse_log(log_file)
    print_summary(counters)

if __name__ == '__main__':
    main()