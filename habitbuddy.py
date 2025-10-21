"""
HabitBuddy 🕒
A simple CLI Habit Tracker — perfect for Hacktoberfest contributions.

Features:
- Add new habits
- Mark habits as done (tracks daily streaks)
- View current streaks
- Data stored locally in JSON
"""

import json, os, datetime

FILE = "habits.json"

# Create file if not exists
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump({}, f)

def load_habits():
    with open(FILE) as f:
        return json.load(f)

def save_habits(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_habit(name):
    data = load_habits()
    if name in data:
        print(f"⚠️  '{name}' already exists.")
        return
    data[name] = {"streak": 0, "last_done": None}
    save_habits(data)
    print(f"✅ Habit '{name}' added successfully!")

def mark_done(name):
    data = load_habits()
    if name not in data:
        print("❌ Habit not found.")
        return
    today = str(datetime.date.today())
    if data[name]["last_done"] != today:
        data[name]["streak"] += 1
        data[name]["last_done"] = today
        save_habits(data)
        print(f"🔥 '{name}' streak updated: {data[name]['streak']} days")
    else:
        print("✅ Already marked as done today!")

def list_habits():
    data = load_habits()
    if not data:
        print("📭 No habits found. Add one to get started!")
        return
    print("\nYour Habits:")
    for name, info in data.items():
        print(f"• {name}: 🔥 {info['streak']} days (last done: {info['last_done']})")

def delete_habit(name):
    data = load_habits()
    if name in data:
        del data[name]
        save_habits(data)
        print(f"🗑️  Habit '{name}' deleted.")
    else:
        print("❌ Habit not found.")

def main():
    while True:
        print("\n=== HabitBuddy Menu ===")
        print("1️⃣  Add Habit")
        print("2️⃣  Mark Done")
        print("3️⃣  List Habits")
        print("4️⃣  Delete Habit")
        print("5️⃣  Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            add_habit(input("Enter habit name: ").strip())
        elif choice == "2":
            mark_done(input("Enter habit name: ").strip())
        elif choice == "3":
            list_habits()
        elif choice == "4":
            delete_habit(input("Enter habit name: ").strip())
        elif choice == "5":
            print("👋 Goodbye! Keep building your habits strong!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
