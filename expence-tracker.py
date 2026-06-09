import csv
import os
import matplotlib.pyplot as plt

FILE = "expenses.csv"


if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Amount", "Category"])


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, amount, category])

    print("Expense added successfully ✅")


def view_expenses():
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def show_summary():
    total = 0
    category_sum = {}

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            amt = float(row["Amount"])
            total += amt

            cat = row["Category"]
            category_sum[cat] = category_sum.get(cat, 0) + amt

    print("\nTotal Expense:", total)
    return category_sum


def plot_chart(data):
    categories = list(data.keys())
    values = list(data.values())

    plt.bar(categories, values)
    plt.title("Expense Breakdown")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig("expense_chart.png")
    plt.show()


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Summary")
    print("4. Show Chart")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        data = show_summary()

    elif choice == "4":
        data = show_summary()
        plot_chart(data)

    elif choice == "5":
        print("Bye 👋")
        break

    else:
        print("Invalid choice ❌")
