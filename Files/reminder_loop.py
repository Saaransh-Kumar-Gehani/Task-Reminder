import time
import psutil
import os
import sys
from datetime import datetime
from plyer import notification
from task_manager import TaskManager


# Encoding
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')


# Checks if the script is running in venv
def is_venv():
    if sys.prefix != sys.base_prefix:
        return True
    return False


# Checks if another reminder_loop.py is running
def is_reminder_loop_running():
    current = psutil.Process(os.getpid())
    parent = current.parent()

    if is_venv():
        skip_pid = [current.pid, parent.pid]
    else:
        skip_pid = [current.pid]

    for p in psutil.process_iter(["name", "cmdline"]):

        try:
            cmdline = " ".join(p.info["cmdline"])
            if "reminder_loop.py" in cmdline and p.pid not in skip_pid:
                return True
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, TypeError):
            continue
        
    return False


# If another file is running, quit
if is_reminder_loop_running():
    quit()


# The main function
def check_tasks():
    manager = TaskManager()
    print("🔄 Task reminder running... (Ctrl+C to stop)")

    while True:
        manager.load_tasks()
        now = datetime.now().strftime("%I:%M%p")
        for task in manager.tasks:
            if task["reminder"] and not task["done"] and task["time"] == now:
                notification.notify(
                    title="⏰ Task Reminder",
                    message=f'{task["description"]} at {task["time"]}',
                    timeout=10
                )
                print(f"🔔 Reminder: {task['description']} at {task['time']}")
                task["done"] = True
                manager.save_tasks()
        time_until_next_minute = 60 - datetime.now().second
        time.sleep(time_until_next_minute)


if __name__ == "__main__":
    check_tasks()