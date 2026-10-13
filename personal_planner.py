from datetime import datetime

BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

file_name = "personal.planner"
tasks = []

def save_tasks():
    pass

def load_tasks():
    try:
        with open(file_name, "rb") as file:
            return []
    except FileNotFoundError:
        return []

def get_valid_time():
    while True:
        time = input(CYAN + "⏱️Enter time(HH:MM AM/PM): " + RESET).strip().upper()
        try:
            datetime.strptime(time, "%I:%M %p")
            return time
        except ValueError:
            print(RED + "❌Invalid time! Example:09:30 AM" + RESET)

def add_task():
    print("\n" + CYAN + "➕ add new task" + RESET)
    time = get_valid_time()
    task_name = input(CYAN + "📝Enter task:" + RESET).strip()
    new_task = {"time": time, "task": task_name}
    tasks.append(new_task)
    save_tasks()
    print(GREEN + "✅ Task added successfully!" + RESET)

def view_tasks():
    if len(tasks) == 0:
        print(YELLOW + "\n No tasks scheduled." + RESET)
        return
    print(BLUE + "\n==========🗓️ MY schedule ==========" + RESET)
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. ⏰ {task['time']} - {task['task']}")
    print(BLUE + "===============================" + RESET)
