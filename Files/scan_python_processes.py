import psutil
from datetime import datetime


# Variables
LOG_FILE = "Files/Other Files/process_log.txt"


# Writes the current running python processes into the file
def log_process_info():
    with open(LOG_FILE, "w") as f:
        f.write(f"\n=== Scan at {datetime.now()} ===\n")

        found = False
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if proc.info['name'] == "python.exe" or proc.info['name'] == "python":
                    cmdline = " ".join(proc.info['cmdline'])
                    f.write(f"PID: {proc.info['pid']} | CMD: {cmdline}\n")
                    found = True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        if not found:
            f.write("No active Python processes found.\n")


if __name__ == "__main__":
    log_process_info()
    print("Log has been written.")