# 🧠 Task Reminder

A lightweight, terminal-based task reminder app written in Python.  
It helps you stay focused by reminding you of tasks at the exact time using desktop notifications — all while running silently in the background.

---

## ✨ Features

- ⏰ Time-based task reminders with desktop notifications
- 🧠 Automatically launches background reminder loop from `main.py`
- 🔁 Prevents multiple `reminder_loop.py` processes using `psutil`
- 💥 Emoji-safe UTF-8 output
- 💻 Works inside or outside virtual environments (`venv`)
- 📁 Tasks saved persistently in a JSON file
- 🧹 Clean CLI with flags for flexibility and silent operation

---

## 📁 Project Structure
``
task-reminder/
├── Files/                         # All source code
│   ├── main.py                   # CLI entry point
│   ├── reminder_loop.py          # Background reminder logic
│   ├── task_manager.py           # Task storage & management
│   ├── scan_python_processes.py  # Debug tool (optional)
│   └── kill_reminders.py         # Debug tool (Kill all running reminder_loop.py)
│
├── Other Files/                  # Other text/log files
│   └── process_log.txt
│
├── requirements.txt              # Python dependencies
├── changelog.md                  # Version history and dev notes
└── README.md                     # Project overview, usage, and structure
``
---

## ▶️ Usage

### 1. Install requirements
- `pip install -r requirements.txt`


### 2. Run the App
- `python Files/main.py`

    ### ➕ Add a task
    - `python Files/main.py add "Do coding" "05:00PM"`

    ### 📋 List all tasks
    - `python Files/main.py list`

    ### ✅ Mark a task as done
    - `python Files/main.py done <task_number>`

    ### 🧪 Suppress background reminder loop (dev mode)
    - `python Files/main.py --no-reminder`


## 🔁 Reminder Loop System
- Runs silently in the background
- Checks every minute
- Uses plyer to show desktop notifications
- Uses psutil to prevent duplicate background loops
- Can be force-killed with:
    - `python Files/kill_reminders.py`


## 🛠 Requirements
- Python 3.7+
- psutil
- plyer
- Install them with:
    - `pip install -r requirements.txt`


## 🗓️ Current Version

- v0.6.4 – Process Detection Fix & UTF-8 Encoding
    - Fixed false-positive duplicate detection in venv and editor environments
    - Used skip_pid logic to avoid killing own parent
    - UTF-8 output reconfigured for emoji-safe terminal handling
    - Stable, clean, and ready for publishing
    - See full history in [Changelog 📜](./changelog.md)


## 🧾 Notes
- Tasks are saved in Files/storage.json (auto-created)
- Emoji support works in most terminals if UTF-8 is enabled
- Reminder loop runs silently without popping open windows
- Check file location Variables carefully


## 📃 License
- (No license currently) — Feel free to view the code.
- Use or modify at your own risk unless a license is added later.
