import pandas as pd

students = pd.read_csv("data/students.csv")
jobs = pd.read_csv("data/jobs.csv")

def calculate_match(student_id, job_id):

    student = students[students["student_id"] == student_id].iloc[0]
    job = jobs[jobs["job_id"] == job_id].iloc[0]

    reasons = []
    matched_features = 0

    features = [
        "java",
        "python",
        "react",
        "communication",
        "projects"
    ]

    total_features = len(features)

    for feature in features:

        student_value = student[feature]
        required_value = job[feature]

        if student_value >= required_value:
            matched_features += 1
            reasons.append(f"{feature} requirement met")

    score = round((matched_features / total_features) * 100)

    if score >= 80:
        level = "Strong Match"
    elif score >= 60:
        level = "Moderate Match"
    else:
        level = "Weak Match"

    return {
        "student": student_id,
        "job": job_id,
        "match_score": score,
        "match_level": level,
        "reasons": reasons
    }