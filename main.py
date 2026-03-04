import subprocess
import time
import re

def check_latency(host):
    result = subprocess.run(
        ["ping", "-c", "1", host],
        capture_output=True,
        text=True
    )

    output = result.stdout
    match = re.search(r'time=(\d+\.\d+)', output)

    if match:
        latency = match.group(1)
        print(f"Latency to {host}: {latency} ms")
    else:
        print("Could not determine latency.")

if __name__ == "__main__":
    host = input("Enter website: ")

    while True:
        check_latency(host)
        time.sleep(2)
