MAX_DELTA = 2
MIN_GRADE = 38
DIVISOR = 5

def gradingStudents(grades):
    rounded_grades = []

    for i in range(len(grades)):
        grade = grades[i]
        rounded_grade = grade

        if grade >= MIN_GRADE:
            delta = DIVISOR - (grade % DIVISOR)

            if delta <= MAX_DELTA:
                rounded_grade = grade + delta

        rounded_grades.insert(i, rounded_grade)

    return rounded_grades   