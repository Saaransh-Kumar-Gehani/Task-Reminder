== Task Reminder – Changelog ==

# [v0.1] – Initial CLI setup
- Created a basic command-line app using `argparse`.
- Added commands: add, list, done.
- Tasks saved in memory only.

# [v0.2] – JSON storage added
- Implemented persistent task saving via `storage.json`.
- Tasks now remain across sessions.
- Introduced `TaskManager` class in a separate module.

# [v0.3] – Reminder engine (first version)
- Created a reminder loop that checks tasks every minute.
- Used `plyer` to trigger desktop notifications.
- Marked tasks as `done` after notifying.
- Basic functional task reminder working.

# [v0.4] – Time formatting & sync fix
- Realized format mismatch between "5:50 PM" and "05:50 PM".
- Improved reminder loop to sync exactly with the start of each minute using:
    `time_until_next_minute = 60 - datetime.now().second`

# [v0.5] – Reflection & refinement
- Reviewed and understood inner workings of `datetime` and `plyer`.
- Verified how notifications are managed and tasks marked as done.
- Debugged a manual syntax error (missed line) using code understanding.
- Confirmed working state of current version.

# [v0.6] - Automating `reminder_loop.py`
- Imported `subprocess` and `sys`.
- Parsed `--no-reminder`, optional flag, defaults to `false`.
- `main.py` automatically calls `reminder_loop.py` when needed.

    ## [v0.6.1] – Subprocess polish
    - Switched to using `creationflags=subprocess.CREATE_NO_WINDOW` for cleaner background launching.
    - Reminder loop now runs without blocking terminal.

    ## [v0.6.2] - Bug fixes
    - Resolved a critical issue where tasks added after the reminder loop started were being lost.
    - Bug was due to `reminder_loop.py` using an outdated in-memory task list and overwriting the storage file.
    - Added `manager.load_tasks()` inside the loop to refresh task list on every cycle.

    ## [v0.6.3] – Reminder loop process control (psutil-based)
    - Used `psutil`.
    - Added `scan_python_processes.py` to scan python processes and record them in `process_log.txt`.
    - Added `kill_reminders.py` to kill all the processes that include `cmdline - 'reminder_loop.py'`.
    - Added `is_reminder_loop_running()` in `reminder_loop.py` that checks if `reminder_loop.py` is already running, quits python if `True`.
    - `is_reminder_loop_running()` is not able to detect if any `reminder_loop.py` is running or not.
    - Managed `TypeError` while using `" ".join(proc.info['cmdline']`.

    ## [v0.6.4] – Process Detection Fix & UTF-8 Encoding  
    - Fixed a bug where `is_reminder_loop_running()` incorrectly detected its own parent as a duplicate `reminder_loop.py` instance.
    - Introduced `skip_pid` logic to safely ignore the current process and its direct parent.
    - Added `is_venv` check to determine if the script is running inside a virtual environment, helping prevent misidentification of duplicate processes.
    - Explicitly set the encoding of `reminder_loop.py` to UTF-8 using `sys.stdout.reconfigure()`, resolving Unicode errors caused by emojis and subprocess redirection.


# == Next Planned Features ==
- Add "pre-reminder" X minutes before actual task time.
- Optionally open VS Code when coding task starts.
- Possibly block distracting apps/websites.
- Add repeatable tasks (daily, weekly).
- Optional sound or snooze option.
- Works from Startup.
- Could use UUID in tasks.

