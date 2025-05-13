#!/usr/bin/env python3

import argparse
import json

def main():
    parser = argparse.ArgumentParser(
        description="Task Tracker CLI App"
    )

    parser.add_argument(
        "command", 
        type=str, 
        help="Command to execute (add, remove, list)"
    )

    args = parser.parse_args()

    if args.command in ["add", "remove"]:
        parser.add_argument(
            "new_task",
            type=str,
            help="Task to add/remove"
        )
    elif args.command == "list":
        parser.add_argument(
            "--list",
            action="store_true",
            help="List all tasks"
        )
    else:
        print("Invalid command. Use 'add', 'remove', or 'list'.")
        return
    
    args = parser.parse_args()
        
    # switch case for command
    if args.command == "add":
        print(f"Task added: {args.new_task}")
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
                tasks["tasks"].append(args.new_task)
        except FileNotFoundError:
            tasks = {"tasks": [args.new_task]}
        
        try:
            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=4, sort_keys=True, ensure_ascii=False)
            print(f"Task '{args.new_task}' added successfully.")
        except IOError as e:
            print(f"Error writing to file: {e}")

    elif args.command == "remove":
        print(f"Task removed: {args.new_task}")
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
                tasks["tasks"].remove(args.new_task)
        except FileNotFoundError:
            print("No tasks found.")
            return
        except ValueError:
            print(f"Task '{args.new_task}' not found.")
            return

        try:
            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=4, sort_keys=True, ensure_ascii=False)
            print(f"Task '{args.new_task}' removed successfully.")
        except IOError as e:
            print(f"Error writing to file: {e}")

    elif args.command == "list":
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
                print(f"Tasks: {tasks['tasks']}")
        except FileNotFoundError:
            print("No tasks found.")
            return
        except ValueError:
            print(f"Task '{args.new_task}' not found.")
            return

if __name__ == "__main__":
    main()