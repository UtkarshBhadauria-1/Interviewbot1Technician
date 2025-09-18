# main.py

from fastapi import FastAPI, Query, Body
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any
import json
import os
from services.scoring import simple_score, score_multiple_answers
from Model import generate_answer, analyze_answer

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load questions from JSON file for efficiency
questions_data = {}
questions_file = "data/questions.json"
if os.path.exists(questions_file):
    with open(questions_file, "r") as f:
        questions_data = json.load(f)

# Role list - expanded to match JSON keys
roles = list(questions_data.keys()) if questions_data else [
    "Web Developer", "Data Scientist", "UI/UX Designer", "DevOps Engineer",
    "Product Manager", "Mobile App Developer", "QA Tester", "System Administrator",
    "AI/ML Engineer", "Cybersecurity Analyst", "Cloud Architect", "Business Analyst",
    "Database Administrator", "Game Developer", "Technical Writer", "IT Support Specialist",
    "Network Engineer", "Embedded Systems Engineer", "Blockchain Developer", "AR/VR Developer",
    "Digital Marketing Specialist", "SEO Analyst", "Content Strategist", "Scrum Master",
    "Software Architect", "Full Stack Developer", "Front End Developer", "Back End Developer",
    "Site Reliability Engineer", "E-commerce Developer"
]

# Default fallback questions
def default_questions(role: str) -> List[Dict[str, Any]]:
    return [
        {
            "question": f"What are the key responsibilities of a {role}?",
            "hint": "Mention tools, workflows, and challenges specific to this role.",
            "difficulty": "Easy"
        },
        {
            "question": f"What skills are essential for a successful {role}?",
            "hint": "Talk about technical and soft skills relevant to the role.",
            "difficulty": "Medium"
        }
    ]

@app.get("/roles", response_model=List[str])
def get_roles():
    return roles

@app.get("/questions", response_model=List[Dict[str, Any]])
def get_questions(role: str = Query(...), limit: int = Query(10, description="Number of questions to return")):
    # Normalize role key to match JSON (lowercase)
    role_key = role.lower()
    if role_key in questions_data:
        questions = questions_data[role_key]
        formatted_questions = []
        for q in questions[:limit]:
            formatted_questions.append({
                "question": q["text"],
                "hint": ", ".join(q.get("ideal_points", [])),
                "difficulty": "Medium"
            })
        return formatted_questions
    else:
        return default_questions(role)

@app.post("/score", response_model=Dict[str, str])
def score_answer(answer: str = Body(...)):
    return simple_score(answer)

@app.post("/score_multiple", response_model=Dict[str, str])
def score_multiple(answers: List[str] = Body(...)):
    """
    A temporary fix to ensure the frontend receives a valid JSON response.
    This bypasses the issue with the 'score_multiple_answers' function.
    """
    return {
        "level": "Good",
        "tip": "This is a placeholder message from the backend. Your answers were submitted successfully!"
    }

@app.post("/generate_answer", response_model=Dict[str, str])
def generate_model_answer(role: str = Body(...), question: str = Body(...)):
    answer = generate_answer(question, role)
    return {"answer": answer}

@app.post("/analyze_answer", response_model=Dict[str, str])
def analyze_user_answer(role: str = Body(...), question: str = Body(...), user_answer: str = Body(...)):
    model_answer = generate_answer(question, role)
    analysis = analyze_answer(user_answer, model_answer)
    return analysis