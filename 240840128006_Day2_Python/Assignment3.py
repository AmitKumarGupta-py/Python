def calculate_final_grade():
    student_name = input("Enter the student's name: ")

    homework_score = float(input("Enter homework score (out of 100): "))
    quizzes_score = float(input("Enter quizzes score (out of 100): "))
    midterm_score = float(input("Enter midterm score (out of 100): "))
    final_exam_score = float(input("Enter final exam score (out of 100): "))

    final_grade = (homework_score * 0.2) + (quizzes_score * 0.2) + (midterm_score * 0.3) + (final_exam_score * 0.3)

    if final_grade >= 90:
        letter_grade = "A"
    elif final_grade >= 80:
        letter_grade = "B"
    elif final_grade >= 70:
        letter_grade = "C"
    elif final_grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    print(f"{student_name}'s final grade is: {final_grade:.2f}% ({letter_grade})")

calculate_final_grade()