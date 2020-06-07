"""
Program: average_scores.py
Author: Jacob Sharpe
Last date modified: 6/06/2020

The purpose of this program is to accept input on a student
and their grades and output the average of 3 grades
"""


def average():
    score1 = input('input score 1: ')
    score1 = float(score1)
    score2 = input('input score 2: ')
    score2 = float(score2)
    score3 = input('input score 3: ')
    score3 = float(score3)

    AvgScore = (score1 + score2 + score3) / 3

    return AvgScore


if __name__ == '__main__':
    last_name = input("enter student's last name: ")
    first_name = input("enter student's first name: ")
    age = input("enter student's age: ")
    average_score = average()
    print("{0}, {1} age: {2} average grade: {3:.2f}".format(last_name, first_name, age, average_score))

# Input       Expected Output  Actual Output
# 90,90,90          90.00         90.00
# 38,97,62          65.66         65.67
# 85,90,95          90.00         90.00
# 'hello'           error          error