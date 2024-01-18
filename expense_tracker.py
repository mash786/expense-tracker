import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, "r") as file:
                self.expenses = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.expenses = {"categories": {}, "entries": []}

    def save_expenses(self):
        with open(self.filename, "w") as file:
            json.dump(self.expenses, file, indent=2)

    def add_expense(self, amount, category):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {"date": date, "amount": amount, "category": category}
        self.expenses["entries"].append(entry)

        # Update category total
        self.expenses["categories"].setdefault(category, 0)
        self.expenses["categories"][category] += amount

        self.save_expenses()

    def view_expenses(self):
        if not self.expenses["entries"]:
            print("No expenses found.")
        else:
            for entry in self.expenses["entries"]:
                print(f"{entry['date']} - ${entry['amount']} ({entry['category']})")

    def view_spending_patterns(self):
        if not self.expenses["categories"]:
            print("No spending patterns found.")
        else:
            for category, total_amount in self.expenses["categories"].items():
                print(f"{category}: ${total_amount}")


def main():
    expense_tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Application")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Spending Patterns")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            amount = float(input("Enter the expense amount: $"))
            category = input("Enter the expense category: ")
            expense_tracker.add_expense(amount, category)
        elif choice == "2":
            expense_tracker.view_expenses()
        elif choice == "3":
            expense_tracker.view_spending_patterns()
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
