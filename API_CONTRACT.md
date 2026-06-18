# Matching API Contract

Endpoint:

GET /match/{student_id}/{job_id}

Example:

GET /match/S1/J1

Response:

{
  "student": "S1",
  "job": "J1",
  "match_score": 100,
  "reasons": [
    "java requirement met",
    "python requirement met",
    "react requirement met",
    "communication requirement met",
    "projects requirement met"
  ]
}