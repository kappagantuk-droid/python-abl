#UNIVERSITY SCHOLARSHIP
n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter student details")
    sid = input("Student ID: ")
    agg = float(input("Aggregate percentage: "))
    sub = float(input("Subject marks: "))
    att = float(input("Attendance percentage: "))
    income = float(input("Family annual income: "))

    if agg >= 75 and sub >= 60 and att >= 75 and income <= 250000:
        print("Student:", sid)
        print("Scholarship Eligible")
    else:
        print("Student:", sid)
        print("Not Eligible")
