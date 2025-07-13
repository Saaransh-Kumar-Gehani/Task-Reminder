import argparse
import subprocess
import sys
from task_manager import TaskManager

# Variables
reminder_loop = "Files\\reminder_loop.py"
storage_file = "Files\\storage.json"


# Early parse to check if --no-reminder is given
early_parser = argparse.ArgumentParser(add_help=False)
early_parser.add_argument('--no-reminder', action='store_true')
early_args, remaining_args = early_parser.parse_known_args()


# If not disabled, run the reminder loop
if not early_args.no_reminder:
    subprocess.Popen(
    [sys.executable, reminder_loop]
)


def main():
    parser = argparse.ArgumentParser(description="Task Notifier CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")
    add_parser.add_argument("time", type=str, help="Time of task (e.g. 10:30 PM)")

    # List command
    list_parser = subparsers.add_parser("list", help="List all tasks")

    # Done command
    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("index", type=int, help="Task number to mark as done (1-based)")

    args = parser.parse_args(remaining_args)
    manager = TaskManager(storage_file=storage_file)

    if args.command == "add":
        manager.add_task(args.description, args.time, not early_args.no_reminder)
        print("✅ Task added.")

    elif args.command == "list":
        tasks = manager.list_tasks()
        if not tasks:
            print("📭 No tasks found.")
        else:
            print("📋 Your Tasks:")
            for t in tasks:
                print(t)

    elif args.command == "done":
        manager.mark_done(args.index - 1)
        print(f"✅ Task #{args.index} marked as done.")

if __name__ == "__main__":
    main()
