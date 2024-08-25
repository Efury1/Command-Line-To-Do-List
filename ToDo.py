import sys

# ANSI color codes for a minimalist and clean look
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
GREY = "\033[90m"
WHITE = "\033[97m"
LIGHT_BLUE = "\033[94m"
LIGHT_GREEN = "\033[92m"
LIGHT_RED = "\033[91m"
LIGHT_CYAN = "\033[96m"

def show_help():
    print(f"\n{BOLD}{LIGHT_CYAN}To-Do List Command Line App{RESET}")
    print(f"{LIGHT_CYAN}{'='*40}{RESET}")
    print(f"{LIGHT_GREEN}Commands:{RESET}")
    print(f"{LIGHT_BLUE}  add <task>{RESET}     - {GREY}Add a new task to the list{RESET}")
    print(f"{LIGHT_BLUE}  list{RESET}           - {GREY}List all tasks{RESET}")
    print(f"{LIGHT_BLUE}  done <task_id>{RESET} - {GREY}Mark a task as done{RESET}")
    print(f"{LIGHT_BLUE}  remove <task_id>{RESET} - {GREY}Remove a task from the list{RESET}")
    print(f"{LIGHT_BLUE}  help{RESET}           - {GREY}Show this help message{RESET}")
    print(f"{LIGHT_BLUE}  quit/exit{RESET}      - {GREY}Exit the application{RESET}\n")

def load_tasks():
    try:
        with open("todo.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open("todo.txt", "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

def list_tasks(tasks):
    if not tasks:
        print(f"{LIGHT_RED}No tasks in the list.{RESET}")
    else:
        print(f"\n{BOLD}{LIGHT_CYAN}Your Tasks:{RESET}")
        for i, task in enumerate(tasks, 1):
            print(f"{LIGHT_GREEN}{i}. {task}{RESET}")

def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)
    print(f'{LIGHT_GREEN}Added task:{RESET} "{task}"')

def remove_task(tasks, task_id):
    if 0 < task_id <= len(tasks):
        removed_task = tasks.pop(task_id - 1)
        save_tasks(tasks)
        print(f'{LIGHT_RED}Removed task:{RESET} "{removed_task}"')
    else:
        print(f"{LIGHT_RED}Task ID {task_id} does not exist.{RESET}")

def mark_task_done(tasks, task_id):
    if 0 < task_id <= len(tasks):
        tasks[task_id - 1] += " (done)"
        save_tasks(tasks)
        print(f'{LIGHT_GREEN}Marked task {task_id} as done.{RESET}')
    else:
        print(f"{LIGHT_RED}Task ID {task_id} does not exist.{RESET}")

def welcome_message():
    print(f"\n{BOLD}{LIGHT_CYAN}Welcome to the To-Do List Command Line App!{RESET}")
    print(f"{GREY}Use the following commands to manage your tasks (Add, List, Done, Remove, Help, Quit):{RESET}")

def get_command():
    welcome_message()
    command = input(f"{ITALIC}{LIGHT_CYAN}➜ Enter command:{RESET} ").strip().split()

    if len(command) == 1 and command[0] in ["quit", "exit"]:
        sys.exit(0)

    return command

def process_command(command, tasks):
    if len(command) == 0:
        return

    if command[0] == "add":
        task = " ".join(command[1:])
        add_task(tasks, task)
    elif command[0] == "list":
        list_tasks(tasks)
    elif command[0] == "done":
        if len(command) > 1 and command[1].isdigit():
            task_id = int(command[1])
            mark_task_done(tasks, task_id)
        else:
            print(f"{LIGHT_RED}Please provide a valid task ID.{RESET}")
    elif command[0] == "remove":
        if len(command) > 1 and command[1].isdigit():
            task_id = int(command[1])
            remove_task(tasks, task_id)
        else:
            print(f"{LIGHT_RED}Please provide a valid task ID.{RESET}")
    elif command[0] == "help":
        show_help()
    elif command[0] in ["quit", "exit"]:
        sys.exit(0)
    else:
        print(f"{LIGHT_RED}Unknown command: {command[0]}{RESET}")
        show_help()

def main():
    tasks = load_tasks()

    while True:
        command = get_command()
        process_command(command, tasks)

if __name__ == "__main__":
    main()
