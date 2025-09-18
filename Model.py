from ollama import chat
from services.scoring import simple_score

def generate_answer(question: str, role: str) -> str:
    """
    Generate a model answer for the given question using Ollama.
    """
    prompt = f"As a {role}, provide a detailed and technical answer to the following interview question: {question}"
    try:
        response = chat(
            model='llama3',
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error generating answer: {e}"

def analyze_answer(user_answer: str, model_answer: str) -> dict:
    """
    Analyze the user's answer by comparing it to the model answer and providing feedback.
    """
    # Basic analysis using existing scoring
    score = simple_score(user_answer)

    # Additional LLM-based analysis
    prompt = f"""
    Compare the user's answer to the model answer and provide detailed feedback.

    Model Answer: {model_answer}

    User Answer: {user_answer}

    Provide feedback in the format:
    Level: [Needs Work/Good/Excellent]
    Tip: [Detailed tip]
    Comparison: [How the user answer compares to the model answer]
    """
    try:
        response = chat(
            model='llama3',
            messages=[{'role': 'user', 'content': prompt}]
        )
        analysis = response['message']['content']
        # Parse the analysis (simple parsing)
        lines = analysis.split('\n')
        level = "Good"
        tip = analysis
        comparison = ""
        for line in lines:
            if line.startswith("Level:"):
                level = line.replace("Level:", "").strip()
            elif line.startswith("Tip:"):
                tip = line.replace("Tip:", "").strip()
            elif line.startswith("Comparison:"):
                comparison = line.replace("Comparison:", "").strip()
        return {
            "level": level,
            "tip": tip,
            "comparison": comparison,
            "model_answer": model_answer
        }
    except Exception as e:
        return {
            "level": score["level"],
            "tip": score["tip"],
            "comparison": f"Error in analysis: {e}",
            "model_answer": model_answer
        }