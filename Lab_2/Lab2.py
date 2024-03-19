# file: main.py
import sys
from data_processing import *
from output_functions import *
from filtering_functions import *

def main():



    log_lines = sys.stdin.readlines()

    print(print_response_200(log_lines))

    counts = count_requests_by_code(log_lines)
    print_request_counts(counts)


    total_gigabytes = calculate_total_data_sent(log_lines)
    print_total_data_sent(total_gigabytes)

    largest_path, largest_size = find_largest_resource(log_lines)
    print_largest_resource(largest_path, largest_size)

    image_ratio = calculate_image_download_ratio(log_lines)
    print_image_download_ratio(image_ratio)

if __name__ == "__main__":
    main()
