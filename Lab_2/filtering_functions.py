# file: filtering_functions.py

from datetime import datetime

def print_response_200(log_lines):
    for line in log_lines:
        try:
            code = line.split()[8]
            if code == '200':
                print(line.rstrip())
        except IndexError:
            pass

def print_resources_downloaded_between_22_and_6(log_lines):
    for line in log_lines:
        try:
            timestamp_str = line.split()[3][1:]
            timestamp = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S')
            if 22 <= timestamp.hour or timestamp.hour < 6:
                print(line.rstrip())
        except (IndexError, ValueError):
            pass

def print_resources_downloaded_on_fridays(log_lines):
    for line in log_lines:
        try:
            timestamp_str = line.split()[3][1:]
            timestamp = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S')
            if timestamp.weekday() == 4:  # Friday is represented by 4 in Python's weekday() method
                print(line.rstrip())
        except (IndexError, ValueError):
            pass

def print_requests_from_poland(log_lines):
    for line in log_lines:
        try:
            host = line.split()[0]
            if host.endswith('.pl'):
                print(line.rstrip())
        except IndexError:
            pass
