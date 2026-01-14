import csv
import os

def read_expenses():
    expenses = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, "expenses.csv")

    with open(filename, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row:
                row["Amount"] = float(row["Amount"])
                expenses.append(row)
    return expenses

def analyze_expenses(expenses):
    total_spent = 0
    category_totals = {}

    for exp in expenses:
        total_spent += exp["Amount"]
        category = exp["Category"]

        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += exp["Amount"]

    highest_category = None
    if category_totals:
        highest_category = max(category_totals, key=category_totals.get)


    return total_spent, category_totals, highest_category

def main():
    expenses = read_expenses()

    if not expenses:
        print("No expenses found. Check expenses.csv")
        return

    total, categories, highest = analyze_expenses(expenses)

    print("Total Amount Spent:", total)
    print()
    print("Category-wise Spending:")
    for cat, amt in categories.items():
        print(cat, ":", amt)
    print()

    if highest:
        print("Highest Spending Category:", highest)
    else:
        print("No category data available")


if __name__ == "__main__":
    main()
