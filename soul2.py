# Grade calculator 
#problem : Assign a letter grade based on a student score
#A(90:100),B(80-89),C(70-79),D(60-69),F(below 60)

student_score = 110

if student_score > 100:
    print("Please verify your grade again")

elif student_score >= 90:
    grade = "A"
elif student_score >= 80:
    grade = "B"
elif student_score >= 70:
    grade = "C"
elif student_score >=60:
    grade = "D"
else: grade = "F"



if student_score <= 100:
    print("Your Grade is:", grade)