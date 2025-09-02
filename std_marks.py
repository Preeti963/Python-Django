# WAP to take marks of "english", "computer" and "math" from 5 students
# and display them with total scored
student_info = []

for i in range(1,6):
    print(f"\nEnter marks for students{i}")

    english = int(input("English:"))
    computer= int(input("computer:"))
    math = int(input("math:"))

total= english + computer + math

student = {
     "student_no": i,
     "English": english,
     "Computer": computer,
     "Math": math,
     "total":total
}
student_info.append(student)

print("\nStudents marks and toatl sheet")
for students in student_info:
    print(f"student {student['student_no']}: English={student["English"]},"
          f"Computer={student['Computer']}, Math={student['Math']},"
          f"Total={student['total']}")