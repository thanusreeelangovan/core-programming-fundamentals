# Expense Tracker (Python)

## Description
The Expense Tracker is a simple Python application that reads expense data from a CSV file and performs basic analysis.  
It calculates the total amount spent, shows category-wise spending, and identifies the highest spending category.

This project is intended for beginners to practice file handling, data processing, and basic analytics using Python.

---

## Features
- Reads expense records from a CSV file
- Calculates total expenditure
- Displays category-wise spending
- Identifies highest spending category
- Handles empty or missing data safely

---

## Project Structure
expense_tracker/
├── expense_tracker.py
├── expenses.csv
└── README.md

---

## CSV File Format
The CSV file must follow this format:

Date,Category,Amount,Description


### Example
2024-01-05,Food,250,Lunch
2024-01-06,Transport,100,Bus fare
2024-01-07,Books,500,Reference book

---

## How to Run
Navigate to the project directory and run:

python expense_tracker.py

---

## Sample Output
Total Amount Spent: 850

Category-wise Spending:
Food : 250
Transport : 100
Books : 500

Highest Spending Category: Books

---

## Concepts Used
- File handling with CSV files
- Dictionaries and lists
- Functions and modular programming
- Basic error handling
- Data aggregation

---

## Future Enhancements
- Add monthly and yearly reports
- Export analysis results to a new CSV file
- Add command-line input for adding expenses
- Visualize expenses using charts

---

^X

