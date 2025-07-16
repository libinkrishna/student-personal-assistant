from . import task_manager, chatbot

def run():
    while True:
        print("\nOptions:")
        print("1. Manage Tasks")
        print("2. Ask Academic Question")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task_manager.manage_tasks()
        elif choice == "2":
            chatbot.ask_question()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
