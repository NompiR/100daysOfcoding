student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}

for i in student_scores:
    s = student_scores[i]
    if s >= 91:
        #print(f"Outstanding, {i}")
        student_grades[i] = "Outstanding"
    elif s >= 81:
        #print("Exceeds Expectations")
        student_grades[i] = "Exceeds Expectations"
    elif s >= 71:
        #print("Acceptable")
        student_grades[i] = "Acceptable"
    else:
        #print("Fail")
        student_grades[i] = "Fail"

print(student_grades)