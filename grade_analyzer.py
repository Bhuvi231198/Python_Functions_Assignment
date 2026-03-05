# Name : Bhuvaneshwari Arumugam
# Roll Number : IITP_AIMLTN_2602425
# Assignment : Python Functions and Modularity - Subjective Question

"""Task 1 — Process the Scores"""
def process_scores(students):
    averages = {}
    
    for student in students:
        scores = students[student]
        total = sum(scores)
        avg = round((total/len(scores)),2)
        averages[student] = avg
    
    return averages

"""Task 2 — Classify the Grades"""
def classify_grades(averages):
    classified = {}
    A_THRESHOLD = 90
    B_THRESHOLD = 75
    C_THRESHOLD = 60
    F_THRESHOLD = 59
    grade = None

    for name, avg in averages.items():
        if avg >= A_THRESHOLD:
            grade = "A"
        elif avg >= B_THRESHOLD:
            grade = "B"
        elif avg >= C_THRESHOLD:
            grade = "C"
        elif avg <= F_THRESHOLD:
            grade = "F"
    
        classified[name] = (avg, grade)

    return classified

"""Task 3 — Generate the Report"""
def generate_report(classified, passing_avg=70):
    status = "PASS"
    pass_count = 0
    print("===== Student Grade Report =====")

    for name, (passing_avg, grade) in classified.items():
        if grade == "F":
            status = "FAIL"
        else:
            pass_count += 1
        print(f"{name}     | Avg: {passing_avg} | Grade: {grade} | Status: {status}")
    print("================================")
    return pass_count


"""Main block"""
student_scores = {
    "Alice":[80,85,92,68,74],
    "Bob":[45,70,69,85,90],
    "Clara":[74,30,20,35,42]
}

average_scores = process_scores(student_scores)
classified_grades = classify_grades(average_scores)
pass_count = generate_report(classified_grades)

print(f"Total Students: {len(student_scores)}")
print(f"Passed        : {pass_count}")
print(f"Failed        : {len(student_scores) - pass_count}")











    
