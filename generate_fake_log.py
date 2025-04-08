"""
File: generate_fake_log.py
Author: Max Ceban
Date: 2025-04-08
Description: This script generates a fake log file with random data. The log file will contain
"""

import random
from datetime import datetime, timedelta


METHODS = ["GET", "POST", "PUT", "DELETE"]
PATHS = ['/index.html', '/about', '/contact', '/products', '/services']
STATUSES = [200, 404, 500, 403]
IPS = ['192.168.1.1', '10.0.0.2','172.16.0.3','127.0.0.1', '8.8.8.8']

def generate_log_line():
    """Generate a single log line with random data"""
    ip = random.choice(IPS)
    now = datetime.now() - timedelta(minutes=random.randint(0, 1440))
    dt = now.strftime('%d/%b/%Y:%H:%M:%S +0000')
    method = random.choice(METHODS)
    path = random.choice(PATHS)
    status = random.choice(STATUSES)
    size = random.randint(100, 10000)

    return f'{ip} - - [{dt}] "{method} {path} HTTP/1.1" {status} {size}\n'

def write_fake_logs(file_path = 'acess.log', num_lines = 1000):
    """Write fake log lines to a file"""
    with open(file_path, 'w') as f:
        for _ in range(num_lines):
            f.write(generate_log_line() + '\n')
    print(f'Generated {num_lines} fake log lines in {file_path}')

if __name__ == '__main__':
    write_fake_logs()