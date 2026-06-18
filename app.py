from fastapi import FastAPI
from matching import calculate_match

app = FastAPI()

@app.get("/")
def home():
    return {"message": "PlaceMux Matching API"}

@app.get("/match/{student_id}/{job_id}")
def match(student_id: str, job_id: str):

    result = calculate_match(
        student_id,
        job_id
    )

    return result