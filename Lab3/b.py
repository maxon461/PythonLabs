def sort_logs(logs, sort_key):
    try:
        sorted_logs = sorted(logs, key=lambda x: x[sort_key])
        return sorted_logs
    except IndexError:
        print("Error: Sort key is out of range.")
        return []

def get_entries_by_addr(logs, address):
    filtered_entries = []
    for log in logs:
        if log[0] == address:
            filtered_entries.append(log)
    return filtered_entries


def get_entries_by_code(logs, code):
    if not isinstance(code, int):
        raise ValueError("status musi miec typ int")

    filtered_entries = list(filter(lambda log: log[3] == code, logs))
    return filtered_entries


def get_failed_reads(logs, combine=False):
    status4 = []
    status5 = []
    for log in logs:
        status_code = log[3]
        if status_code.startswith('4'):
            status4.append(log)
        elif status_code.startswith('5'):
            status5.append(log)

    if combine:
        failed_reads = status4 + status5
        return failed_reads
    else:
        return status4, status5

def get_entries_by_extension(logs, extension):

    filtered_entries = []
    for log in logs:
        request = log[2]
        if request.endswith("." + extension):
            filtered_entries.append(log)

    return filtered_entries

def display_entries(logs):
    for log in logs:
        print(log)

