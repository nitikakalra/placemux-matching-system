# PlaceMux Matching System

## Project Overview

This project was developed as part of the PlaceMux AI/ML Engineer Phase 2 task.

The goal of the project is to match students with jobs based on their verified skills and job requirements. The system compares student scores with job expectations and generates a match score along with reasons for the recommendation.

## Features

* Student and job feature matching
* Match score calculation
* Strong Moderate and Weak match levels
* Explainable matching results
* FastAPI based REST API
* Interactive API testing using Swagger UI

## Feature Space

### Student Features

* Java Score
* Python Score
* React Score
* Communication Score
* Projects Count

### Job Features

* Required Java Score
* Required Python Score
* Required React Score
* Required Communication Score
* Required Projects Count

## Matching Logic

The system compares each student feature with the corresponding job requirement.

If the student score is equal to or greater than the required score then that feature is considered matched.

Match Score = (Matched Features / Total Features) × 100

Based on the score the candidate is classified as:

* Strong Match
* Moderate Match
* Weak Match

## Project Structure

```text
placemux-matching
│
├── data
│   ├── students.csv
│   └── jobs.csv
│
├── app.py
├── matching.py
├── FEATURE_SPACE.md
├── API_CONTRACT.md
├── README.md
└── requirements.txt
```

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Move to the project folder

```bash
cd placemux-matching
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

```bash
venv\Scripts\activate
```

Install the required packages

```bash
pip install -r requirements.txt
```

## Run the Application

Start the FastAPI server

```bash
python -m uvicorn app:app --reload
```

Open the API documentation

```text
http://127.0.0.1:8000/docs
```

## Example Request

```text
GET /match/S1/J1
```

## Example Response

```json
{
  "student": "S1",
  "job": "J1",
  "match_score": 100,
  "match_level": "Strong Match",
  "reasons": [
    "java requirement met",
    "python requirement met",
    "react requirement met",
    "communication requirement met",
    "projects requirement met"
  ]
}
```

## Future Improvements

* Support multiple job recommendations
* Candidate ranking system
* Machine learning based matching
* Better evaluation metrics
* Real database integration

## Author

Nitika Kalra

AI ML Engineer Intern

PlaceMux Phase 2
