import psutil


# Kills all the currently running files, use if cluttered
def kill_reminder_loops():
    for proc in psutil.process_iter(['pid', 'cmdline']):
        try:
            if "reminder_loop.py" in " ".join(proc.info['cmdline']):
                proc.kill()
        except TypeError:
            continue
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass


if __name__ == "__main__":
    kill_reminder_loops()
    print("Killed all the processes.")