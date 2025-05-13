#!/usr/bin/env python3

import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f).get("tasks", [])
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump({"tasks": tasks}, f, indent=4, sort_keys=True, ensure_ascii=False)


def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task '{task}' added.")


def remove_task(task):
    tasks = load_tasks()
    if task in tasks:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"✅ Task '{task}' removed.")
    else:
        print(f"❌ Task '{task}' not found.")


def list_tasks():
    tasks = load_tasks()
    if tasks:
        print("📋 Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("📭 No tasks found.")


def show_help():
    print("""
Available commands:
  add <task>      Add a new task
  remove <task>   Remove an existing task
  list            List all tasks
  help            Show this help message
  exit            Exit the program
""")


def main():
    print("🚀 Welcome to the Task Tracker CLI App!")
    show_help()

    while True:
        try:
            user_input = input("\n> ").strip()
            if not user_input:
                continue

            parts = user_input.split(maxsplit=1)
            command = parts[0].lower()
            argument = parts[1] if len(parts) > 1 else None

            if command == "add":
                if not argument:
                    print("⚠️  Please provide a task to add.")
                    continue
                add_task(argument)

            elif command == "remove":
                if not argument:
                    print("⚠️  Please provide a task to remove.")
                    continue
                remove_task(argument)

            elif command == "list":
                list_tasks()

            elif command == "help":
                show_help()

            elif command == "exit":
                print("👋 Goodbye!")
                break

            else:
                print(f"❓ Unknown command: '{command}' (type 'help' for list of commands)")

        except KeyboardInterrupt:
            print("\n👋 Exiting Task Tracker. Goodbye!")
            break


if __name__ == "__main__":
    main()
