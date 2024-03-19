
from read import *
from c import *
from b import *


def print_log_dict(log_dict):
    for ip_or_host, entries in log_dict.items():
        print(f"Adres IP lub nazwa hosta: {ip_or_host}")
        for entry in entries:
            print("\tWpis:")
            for key, value in entry.items():
                print(f"\t\t{key}: {value}")


if __name__ == "__main__":
    logs = read_log()
    sorted_logs = get_entries_by_code(logs, 304)
    # display_entries(sorted_logs)
    map1 = log_to_dict(logs)
    print_dict_entry_dates(map1)

