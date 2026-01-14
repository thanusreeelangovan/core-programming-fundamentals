import csv

def read_data(filename):
    students = []
    filename = r"C:/Users/admin/core-programming-fundamentals/python/data.csv"
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students

def analyze_results(students):
    total_students = len(students)
    pass_count = 0
    fail_count = 0
    topper = None
    highest_total = 0

    for s in students:
        marks = [
            int(s["Physics"]),
            int(s["Maths"]),
            int(s["Electronics"]),
            int(s["CommunicationSkills"]),
            int(s["IDT"]),
            int(s["Kannada"]),
            int(s["CyberSecurity"])
        ]

        total = sum(marks)
        average = total / len(marks)

        s["Total"] = total
        s["Average"] = average

        if average >= 40:
            pass_count += 1
        else:
            fail_count += 1

        if total > highest_total:
            highest_total = total
            topper = s

    return total_students, pass_count, fail_count, topper

def main():
    filename = "data.csv"
    students = read_data(filename)

    total, passed, failed, topper = analyze_results(students)

    print("Total Students:", total)
    print("Passed:", passed)
    print("Failed:", failed)
    print()
    print("Topper Details")
    print("Name:", topper["Name"])
    print("USN:", topper["USN"])
    print("Total Marks:", topper["Total"])
    print("Average:", topper["Average"])

if __name__ == "__main__":
    main()
