import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("data/reminders.json")

def load_reminders():
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    else:
        return []


def save_reminders(reminders):
    with open(DATA_FILE, "w") as f:
        json.dump(reminders, f, indent=4)

def manage_reminders():
    while True:
        print("\nReminder Scheduler:")
        print("1. View Reminders")
        print("2. Add Reminder")
        print("3. Delete Reminder")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            reminders = load_reminders()
            if not reminders:
                print("No reminders found.")
            else:
                for idx, reminder in enumerate(reminders, 1):
                    print(f"{idx}. {reminder['note']} at {reminder['datetime']}")
        elif choice == "2":
            note = input("Enter the reminder note: ")
            date_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
            try:
                dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
                reminders = load_reminders()
                reminders.append({"note": note, "datetime": dt.strftime("%Y-%m-%d %H:%M")})
                save_reminders(reminders)
                print("Reminder added successfully.")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD HH:MM.")
        elif choice == "3":
            reminders = load_reminders()
            if not reminders:
                print("No reminders to delete.")
            else:
                for idx, reminder in enumerate(reminders, 1):
                    print(f"{idx}. {reminder['note']} at {reminder['datetime']}")
                to_delete = int(input("Enter the reminder number to delete: "))
                if 1 <= to_delete <= len(reminders):
                    removed = reminders.pop(to_delete - 1)
                    save_reminders(reminders)
                    print(f"Reminder '{removed['note']}' deleted.")
                else:
                    print("Invalid reminder number.")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
