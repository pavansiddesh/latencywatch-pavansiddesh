import subprocess

def check_latency(host="google.com"):
    result = subprocess.run(["ping", "-c", "4", host], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    check_latency()
