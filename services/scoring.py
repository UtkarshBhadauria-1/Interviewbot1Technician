from typing import Dict

def simple_score(answer: str) -> Dict[str, str]:
    """A beginner-friendly scoring function (no LLM)."""
    if len(answer.split()) < 5:
        return {"level": "Needs Work", "tip": "Try writing longer answers with examples."}
    elif len(answer.split()) < 20:
        return {"level": "Good", "tip": "Great! Add more structure and real-life examples."}
    else:
        return {"level": "Excellent", "tip": "Well explained! Keep this clarity."}
