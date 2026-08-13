student_info={
    "25NO1": {"name": "s1", "roll no": "25NO1", "course": "course1","marks":"mark1" },
    "25NO2": {"name": "s2", "roll no": "25NO2", "course": "course2","marks":"mark2" },
    "25NO3": {"name": "s3", "roll no": "25NO3", "course": "course3","marks":"mark3" }
}
student_roll_no=str(input("enter student roll no: "))
if student_roll_no in student_info:
    print(student_info[student_roll_no])
else:
    print("student not in list")

