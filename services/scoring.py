from typing import Dict, List

def simple_score(answer: str) -> Dict[str, str]:
    """A beginner-friendly scoring function (no LLM)."""
    if len(answer.split()) < 5:
        return {"level": "Needs Work", "tip": "Try writing longer answers with examples and more technical depth."}
    elif len(answer.split()) < 20:
        return {"level": "Good", "tip": "Good start! Add more structure, real-life examples, and technical details."}
    else:
        return {"level": "Excellent", "tip": "Well explained with technical depth! Keep this clarity."}

def score_multiple_answers(answers: List[str]) -> Dict[str, str]:
    """
    Scores multiple answers and provides consolidated feedback with more technical depth.
    """
    total_score = 0
    detailed_tips = []
    for answer in answers:
        words = len(answer.split())
        if words < 5:
            total_score += 1
            detailed_tips.append("Needs more elaboration and examples.")
        elif words < 20:
            total_score += 2
            detailed_tips.append("Good structure but can add more technical details.")
        else:
            total_score += 3
            detailed_tips.append("Excellent explanation with good technical depth.")

    avg_score = total_score / (3 * len(answers))  # Normalize between 0 and 1

    if avg_score < 0.4:
        level = "Needs Work"
        tip = "Your answers are brief. Try to elaborate more with technical details and examples."
    elif avg_score < 0.75:
        level = "Good"
        tip = "Your answers are solid. Focus on adding more technical depth and structured explanations."
    else:
        level = "Excellent"
        tip = "Great job! Your answers show strong technical understanding and clarity."

    consolidated_tip = tip + " Detailed feedback per answer: " + " | ".join(detailed_tips)
    return {"level": level, "tip": consolidated_tip}
