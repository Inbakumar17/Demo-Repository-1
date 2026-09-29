# ISSUE 74
#
# Problem:
# Write a program that accepts student attendance records and calculates each student's attendance percentage and identifies students below a given attendance percentage.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def attendance_report(records, minimum_percent):
    totals = {}
    present = {}
    for record in records:
        student = record["student"]
        totals[student] = totals.get(student, 0) + 1
        # TODO: Check which attendance values count as present.
        if record["status"] != "absent":
            present[student] = present.get(student, 0) + 1
    percentages = {student: present.get(student, 0) / count * 100 for student, count in totals.items()}
    # TODO: Check which students fall below the requested threshold.
    below = [student for student, percent in percentages.items() if percent > minimum_percent]
    # TODO: Check that percentages for all students are returned.
    return percentages, below

def check_solution():
    records = [{"student":"A","status":"present"},{"student":"A","status":"absent"},{"student":"B","status":"present"}]
    assert attendance_report(records, 75) == ({"A":50.0,"B":100.0},["A"])
    assert attendance_report([], 50) == ({},[])

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
