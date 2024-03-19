
def entry_to_dict(entry):
    keys = ["ip", "datetime", "request", "status_code", "size"]
    entry_dict = {keys[i]: entry[i] for i in range(len(keys))}
    return entry_dict

def log_to_dict(logs):
    log_dict = {}
    for entry in logs:
        ip_or_host = entry[0]
        entry_dict = entry_to_dict(entry)
        if ip_or_host in log_dict:
            log_dict[ip_or_host].append(entry_dict)
        else:
            log_dict[ip_or_host] = [entry_dict]
    return log_dict

def get_addrs(log_dict):
    return list(log_dict.keys())


def print_dict_entry_dates(log_dict):
    for addr, entries in log_dict.items():
        num_requests = len(entries)
        first_request_date = entries[0]["datetime"]
        last_request_date = entries[-1]["datetime"]
        num_successful_requests = sum(1 for entry in entries if entry["status_code"] == 200)
        success_rate = num_successful_requests / num_requests if num_requests > 0 else 0

        print(f"Adres IP/nazwa domenowa hosta: {addr}")
        print(f"Liczba żądań wykonanych przez hosta: {num_requests}")
        print(f"Data pierwszego żądania: {first_request_date}")
        print(f"Data ostatniego żądania: {last_request_date}")
        print(f"Stosunek liczby żądań z kodem 200 do wszystkich żądań: {success_rate:.2f}")
        print()
