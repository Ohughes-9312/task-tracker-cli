# -------------------------
# 1. IMPORTS
# -------------------------
import sys
from task_manager import add_task, list_tasks, complete_task, delete_task

# -------------------------
# 2. COLOR CONSTANTS
# -------------------------
RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"

# -------------------------
# 3. HELPER FUNCTIONS
# -------------------------
def safe_int(value):
    """Safely convert a string to an integer."""
    try:
        return int(value)
    except ValueError:
        return None


def show_help():
    """Display available CLI commands."""
    print(f"{BOLD}Task Tracker CLI Commands:{RESET}\n")
    print(f"{CYAN}python main.py add \"task description\"{RESET} - Add a new task")
    print(f"{CYAN}python main.py list{RESET} - List all tasks")
    print(f"{CYAN}python main.py list pending{RESET} - List only pending tasks")
    print(f"{CYAN}python main.py list completed{RESET} - List only completed tasks")
    print(f"{CYAN}python main.py complete <id>{RESET} - Mark a task as complete")
    print(f"{CYAN}python main.py delete <id>{RESET} - Delete a task")
    print()


# -------------------------
# 4. MAIN FUNCTION
# -------------------------
def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1]

    # -------------------------
    # ADD TASK
    # -------------------------
    if command == "add":
        if len(sys.argv) < 3:
            print(f"{RED}Error: Please provide a task description.{RESET}")
            return

        description = " ".join(sys.argv[2:])
        task = add_task(description)
        print(f"{GREEN}Task added successfully!{RESET}")
        print(f"{BOLD}ID:{RESET} {task['id']}")
        print(f"{BOLD}Description:{RESET} {task['description']}")
        print()

    # -------------------------
    # LIST TASKS
    # -------------------------
    elif command == "list":
        tasks = list_tasks()

        # Filtering
        if len(sys.argv) == 3:
            filter_type = sys.argv[2]
            if filter_type == "completed":
                tasks = [t for t in tasks if t["completed"]]
            elif filter_type == "pending":
                tasks = [t for t in tasks if not t["completed"]]

        if not tasks:
            print(f"{YELLOW}No tasks found.{RESET}")
            return

        print(f"{BOLD}{CYAN}Your Tasks:{RESET}\n")

        for task in tasks:
            status = (
                f"{GREEN}✔️ Completed{RESET}"
                if task["completed"]
                else f"{YELLOW}❌ Pending{RESET}"
            )

            print(f"{BOLD}{task['id']}. {task['description']}{RESET}")
            print(f"   Status: {status}")
            print(f"   Created: {task['created_at']}")
            if task["completed_at"]:
                print(f"   Completed: {task['completed_at']}")
            print()

    # -------------------------
    # COMPLETE TASK
    # -------------------------
    elif command == "complete":
        if len(sys.argv) < 3:
            print(f"{RED}Error: Please provide a task ID.{RESET}")
            return

        task_id = safe_int(sys.argv[2])
        if task_id is None:
            print(f"{RED}Error: Task ID must be a number.{RESET}")
            return

        task = complete_task(task_id)
        if task:
            print(f"{GREEN}Task {task_id} marked as complete!{RESET}")
        else:
            print(f"{RED}Error: Task not found.{RESET}")

    # -------------------------
    # DELETE TASK
    # -------------------------
    elif command == "delete":
        if len(sys.argv) < 3:
            print(f"{RED}Error: Please provide a task ID.{RESET}")
            return

        task_id = safe_int(sys.argv[2])
        if task_id is None:
            print(f"{RED}Error: Task ID must be a number.{RESET}")
            return

        success = delete_task(task_id)
        if success:
            print(f"{YELLOW}Task {task_id} deleted.{RESET}")
        else:
            print(f"{RED}Error: Task not found.{RESET}")

    # -------------------------
    # UNKNOWN COMMAND
    # -------------------------
    else:
        print(f"{RED}Unknown command: {command}{RESET}")
        show_help()


# -------------------------
# 5. ENTRY POINT
# -------------------------
if __name__ == "__main__":
    main()