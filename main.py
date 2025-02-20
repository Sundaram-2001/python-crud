import json
from typing import Any

file_path="data.json"
def load_data()->list[dict]:
    """Load JSON data from the file."""
    try:
        with open(file_path,'r') as file:
            return json.load(file)
    except (FileNotFoundError):
        return []
    
def save_data(data:list[dict]):
    """Save data to the JSON file."""
    try:
        with open(file_path,'w') as file:
            json.dump(file,indent=4)
    except (FileNotFoundError):
        print("file not found!")

def add_task()->None:
    try:
        data=load_data()
        new_task={
            "id": len(data) + 1,
            "task": "Buy groceries",
            "completed": "false",
            "priority": "high",
            "dueDate": "2024-03-20"
        }
        data.append(new_task)
        save_data(data)
        print("Task added successfully!")
    except Exception as e:
        print(f"Error adding task: {e}")


