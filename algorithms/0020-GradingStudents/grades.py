MAX_DELTA = 2
MIN_GRADE = 38
DIVISOR = 5

def gradingStudents(grades):
    rounded_grades = []

    for grade in grades:
        delta = DIVISOR - (grade % DIVISOR)
        
        rounded_grade = grade
        if grade >= MIN_GRADE and delta <= MAX_DELTA:
            rounded_grade = grade + delta

        rounded_grades.append(rounded_grade)

    return rounded_grades   