# lab_3_h.py

import sys
from filtering_functions import print_requests_from_poland

def main():
    log_lines = sys.stdin.readlines()
    print_requests_from_poland(log_lines)

if __name__ == "__main__":
    main()
