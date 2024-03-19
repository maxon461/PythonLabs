import sys
from datetime import datetime
def read_log():
    logs = []
    for line in sys.stdin:
        line = line.strip()
        if line:  # Sprawdzenie, czy linia nie jest pusta
            try:
                elements = line.split()

                # Podział na poszczególne elementy
                host = elements[0]
                timestamp = elements[3][1:]  # Łączenie daty i czasu
                timestamp = datetime.strptime(timestamp, "%d/%b/%Y:%H:%M:%S")
                timestamp = timestamp.strftime("%d/%b/%Y:%H:%M:%S")
                request = elements[5] + " " + elements[6] + " " + elements[7]

                try:
                    status_code = int(elements[8])
                except(ValueError):
                    status_code = elements[8]

                try:
                    bytes_sent = int(elements[9])
                except(ValueError):
                    bytes_sent = elements[9]

                logs.append((host, timestamp, request, status_code, bytes_sent))
            except(IndexError):
                pass
    return logs
