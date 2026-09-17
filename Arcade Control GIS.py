print("Arcade Control Desk")

undostack = []

def push_action(action):
    undostack.append(action)
    print(f"Action recorded: {action}")

def undo_last_action():
    if len(undostack) == 0:
        print("Nothing to undo.")
    else:
        removed = undostack.pop()
        print(f"Undid action: {removed}")

player_queue = []

def add_player(name):
    player_queue.append(name)
    print(f"{name} joined the queue.")

def serve_next_player():
    if len(player_queue) == 0:
        print("No players waiting.")
    else:
        served = player_queue.pop(0)
        print(f"Now serving: {served}")

quest_data = []
quest_next = []
quest_head = -1

def add_quest(name):
    global quest_head
    quest_data.append(name)
    quest_next.append(-1)
    new_index = len(quest_data) - 1
    if quest_head == -1:
        quest_head = new_index
    else:
        current = quest_head
        while quest_next[current] != -1:
            current = quest_next[current]
        quest_next[current] = new_index

    print(f"Quest added to chain: {name}")


def show_menu():
    print("\n--- Arcade Control Desk Menu ---")
    print("1. Add action")
    print("2. Undo action")
    print("3. Output action stack")
    print("4. Add player")
    print("5. Serve player")
    print("6. Output player queue")
    print("7. Add quest")
    print("8. Output quest list")
    print("9. Exit")


def run_menu():
    while True:
        show_menu()
        choice = input("Choose an option (1-9): ")

        if choice == "1":
            action = input("Action: ")
            push_action(action)
        elif choice == "2":
            undo_last_action()
        elif choice == "3":
            print(undostack)
        elif choice == "4":
            name = input("Enter player name: ")
            add_player(name)
        elif choice == "5":
            serve_next_player()
        elif choice == "6":
            print(player_queue)
        elif choice == "7":
            quest = input("Enter quest name: ")
            add_quest(quest)
        elif choice == "8":
            print(quest_data)
        elif choice == "9":
            break
        else:
            print("Invalid choice, please enter a number from 1 to 6.")

print("Stack ready")
print("Queue ready")
print("Linked list ready")

run_menu()
