# main.py

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict, Any

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Role list
roles = [
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

# Role-specific questions for first 10 roles
role_questions: Dict[str, List[Dict[str, Any]]] = {
    "Web Developer": [
        {
            "question": "Can you explain the difference between frontend and backend development?",
            "hint": "Mention UI, client-side vs server-side, and technologies like HTML vs Python.",
            "difficulty": "Easy"
        },
        {
            "question": "How do you optimize a website for performance?",
            "hint": "Talk about lazy loading, caching, minification, and CDN usage.",
            "difficulty": "Medium"
        },
        {
            "question": "What is your experience with responsive design?",
            "hint": "Mention media queries, mobile-first design, and frameworks like Bootstrap.",
            "difficulty": "Easy"
        }
    ],
    "Data Scientist": [
        {
            "question": "How do you handle missing data in a dataset?",
            "hint": "Talk about imputation, dropping rows, or using models that handle missing values.",
            "difficulty": "Medium"
        },
        {
            "question": "Explain the bias-variance tradeoff.",
            "hint": "Use examples from model training and overfitting vs underfitting.",
            "difficulty": "Hard"
        },
        {
            "question": "What’s the difference between supervised and unsupervised learning?",
            "hint": "Define both and give examples like regression vs clustering.",
            "difficulty": "Easy"
        }
    ],
    "UI/UX Designer": [
        {
            "question": "How do you approach user research?",
            "hint": "Mention surveys, interviews, usability testing, and empathy maps.",
            "difficulty": "Medium"
        },
        {
            "question": "What tools do you use for prototyping?",
            "hint": "Include Figma, Adobe XD, Sketch, or InVision.",
            "difficulty": "Easy"
        },
        {
            "question": "Describe a time you improved a product’s usability.",
            "hint": "Talk about user feedback, redesigns, and measurable outcomes.",
            "difficulty": "Hard"
        }
    ],
    "DevOps Engineer": [
        {
            "question": "What is CI/CD and why is it important?",
            "hint": "Explain continuous integration and deployment pipelines.",
            "difficulty": "Medium"
        },
        {
            "question": "How do you monitor system performance in production?",
            "hint": "Mention tools like Prometheus, Grafana, or ELK stack.",
            "difficulty": "Hard"
        },
        {
            "question": "What’s your experience with containerization?",
            "hint": "Talk about Docker, Kubernetes, and orchestration.",
            "difficulty": "Medium"
        }
    ],
    "Product Manager": [
        {
            "question": "How do you prioritize features in a product roadmap?",
            "hint": "Mention frameworks like MoSCoW or RICE.",
            "difficulty": "Medium"
        },
        {
            "question": "Describe a time you handled conflicting stakeholder demands.",
            "hint": "Talk about negotiation, compromise, and user focus.",
            "difficulty": "Hard"
        },
        {
            "question": "How do you define product success?",
            "hint": "Include metrics like retention, NPS, or revenue impact.",
            "difficulty": "Easy"
        }
    ],
    "Mobile App Developer": [
        {
            "question": "What are the key differences between native and hybrid apps?",
            "hint": "Mention performance, platform access, and frameworks.",
            "difficulty": "Medium"
        },
        {
            "question": "How do you handle screen size variations?",
            "hint": "Talk about responsive layouts and adaptive UI.",
            "difficulty": "Easy"
        },
        {
            "question": "What’s your experience with app store deployment?",
            "hint": "Include signing, testing, and submission process.",
            "difficulty": "Medium"
        }
    ],
    "QA Tester": [
        {
            "question": "What’s the difference between manual and automated testing?",
            "hint": "Mention tools, speed, and use cases.",
            "difficulty": "Easy"
        },
        {
            "question": "How do you write effective test cases?",
            "hint": "Include clarity, coverage, and edge cases.",
            "difficulty": "Medium"
        },
        {
            "question": "Describe a bug you found and how you reported it.",
            "hint": "Talk about reproduction steps and communication.",
            "difficulty": "Hard"
        }
    ],
    "System Administrator": [
        {
            "question": "How do you ensure system uptime and reliability?",
            "hint": "Mention monitoring, backups, and failover strategies.",
            "difficulty": "Medium"
        },
        {
            "question": "What’s your experience with user access control?",
            "hint": "Include permissions, roles, and audit trails.",
            "difficulty": "Easy"
        },
        {
            "question": "How do you handle patch management?",
            "hint": "Talk about scheduling, testing, and automation.",
            "difficulty": "Medium"
        }
    ],
    "AI/ML Engineer": [
        {
            "question": "What’s the difference between classification and regression?",
            "hint": "Give examples and explain output types.",
            "difficulty": "Easy"
        },
        {
            "question": "How do you prevent overfitting in ML models?",
            "hint": "Mention regularization, cross-validation, and dropout.",
            "difficulty": "Hard"
        },
        {
            "question": "Describe your experience with model deployment.",
            "hint": "Talk about APIs, containers, and scaling.",
            "difficulty": "Medium"
        }
    ],
    "Cybersecurity Analyst": [
        {
            "question": "What is the difference between a vulnerability and an exploit?",
            "hint": "Define both and give examples.",
            "difficulty": "Medium"
        },
        {
            "question": "How do you detect and respond to a security breach?",
            "hint": "Mention incident response plans and tools.",
            "difficulty": "Hard"
        },
        {
            "question": "What’s your experience with penetration testing?",
            "hint": "Include tools, scope, and reporting.",
            "difficulty": "Medium"
        }
    ]
}

@app.get("/roles", response_model=List[str])
def get_roles():
    return roles

@app.get("/questions", response_model=List[Dict[str, Any]])
def get_questions(role: str = Query(...)):
    return role_questions.get(role, default_questions(role))