import csv
import os

def read_data():
    students = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, "data.csv")

    with open(filename, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row and row["USN"]:
                students.append(row)
    return students

def analyze_results(students):
    total_students = len(students)
    pass_count = 0
    fail_count = 0
    topper = None
    highest_total = 0

    # Automatically detect subjects
    subjects = [col for col in students[0] if col not in ("USN", "Name")]

    for s in students:
        marks = [int(s[sub]) for sub in subjects]
        total = sum(marks)
        average = total / len(subjects)

        s["Total"] = total
        s["Average"] = round(average, 2)

        if average >= 40:
            pass_count += 1
        else:
            fail_count += 1

        if total > highest_total:
            highest_total = total
            topper = s

    return total_students, pass_count, fail_count, topper, subjects

def main():
    students = read_data()
    total, passed, failed, topper, subjects = analyze_results(students)

    print("Total Students:", total)
    print("Passed:", passed)
    print("Failed:", failed)
    print()
    print("Topper Details")
    print("Name:", topper["Name"])
    print("USN:", topper["USN"])
    print("Total Marks:", topper["Total"])
    print("Average:", topper["Average"])
    print()
    print("Subject-wise marks:")
    for sub in subjects:
        print(sub + ":", topper[sub])

if __name__ == "__main__":
    main()

