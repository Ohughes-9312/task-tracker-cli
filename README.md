# 📌 Task Tracker CLI

A clean, lightweight, and fully functional command‑line task manager built in Python.
This tool lets you add, list, complete, and delete tasks — all stored locally in a JSON file.
Designed with clarity, modularity, and professional development practices in mind.

## ✨ Features

• Add new tasks
• List all tasks, pending tasks, or completed tasks
• Mark tasks as complete
• Delete tasks
• Persistent incremental task IDs
• Automatic timestamps (, )
• Color‑coded, polished CLI output
• JSON‑based storage (no database required)
• Fully modular architecture
• Optional testing suite using
• Auto‑formatted with Black + isort + flake8

## 📁 Project Structure

task-tracker-cli/
│
├── main.py # CLI interface
├── task_manager.py # Core task logic
├── tasks.json # Local data storage
├── README.md # Project documentation
├── requirements.txt # Development tools
└── tests/
└── test_task_manager.py

## 🖥️ Installation

- Clone the repository
    - git clone <your-repo-url>
    - cd task-tracker-cli
- Create a virtual environment
    - python -m venv .venv
- Activate the environment
    - Windows:
        - .venv\Scripts\activate
    - Mac/Linux:
        - source .venv/bin/activate
- Install dependencies
    - pip install -r requirements.txt

## 🚀 Usage

Run the CLI using:
python main.py <command> [arguments]

Add a task
python main.py add "Buy groceries"

List all tasks
python main.py list

List only pending tasks
python main.py list pending

List only completed tasks
python main.py list completed

Mark a task as complete
python main.py complete 1

Delete a task
python main.py delete 1

## 📦 Task Data Structure

Each task is stored in tasks.json as:

{
"id": 1,
"description": "Buy groceries",
"completed": false,
"created_at": "2026-02-12T16:45:00",
"completed_at": null
}

## 🧪 Running Tests

This project includes a minimal pytest suite.

Run all tests:
pytest

Example test file:

- tests/
    - test_task_manager.py

## 🛠️ Development Tools

This project uses professional Python tooling:

- Black – auto‑formatter
- isort – import sorter
- flake8 – linter
- pytest – testing framework

Install them with:

- pip install black isort flake8 pytest

Format code manually:

- black .
- isort .
- flake8 .

## 📸 Screenshots

/screenshots/

- list.png
- add.png
- complete.png

## 📜 License

MIT License

## 🙌 Author

Okoye Hughes
Task Tracker CLI — 2026



    

