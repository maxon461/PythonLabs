# file: data_processing.py

def count_requests_by_code(log_lines):
    counts = {'200': 0, '302': 0, '404': 0}
    for line in log_lines:
        try:
            code = line.split()[8]
            if code in counts:
                counts[code] += 1
        except IndexError:
            pass
    return counts

def calculate_total_data_sent(log_lines):
    total_bytes = 0
    for line in log_lines:
        try:
            bytes_sent = int(line.split()[9])
            total_bytes += bytes_sent
        except (IndexError, ValueError):
            pass
    total_gigabytes = total_bytes / (1024 ** 3)
    return total_gigabytes

def find_largest_resource(log_lines):
    largest_size = 0
    largest_path = ''
    for line in log_lines:
        try:
            code = line.split()[9]
            size = len(code)
            if size > largest_size:
                largest_size = size
                largest_path = line.split()[6]
        except (IndexError, ValueError):
            pass
    return largest_path, largest_size

def calculate_image_download_ratio(log_lines):
    image_count = 0
    total_count = 0
    for line in log_lines:
        try:
            path = line.split()[6]
            total_count += 1
            if path.endswith(('.gif', '.jpg', '.jpeg', '.xbm')):
                image_count += 1
        except IndexError:
            pass
    if total_count == 0:
        return 0
    return image_count / total_count
