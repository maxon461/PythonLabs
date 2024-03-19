# file: output_functions.py

def print_request_counts(counts):
    for code, count in counts.items():
        print(f'HTTP {code} - Requests: {count}')

def print_total_data_sent(total_gigabytes):
    print(f'Total data sent: {total_gigabytes:.2f} GB')

def print_largest_resource(path, size):
    print(f'Largest resource: {path} - Size: {size} bytes')

def print_image_download_ratio(ratio):
    print(f'Image download ratio: {ratio:.2%}')
