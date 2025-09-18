import requests

BASE_URL = "http://localhost:8000"

def test_generate_answer():
    url = f"{BASE_URL}/generate_answer"
    payload = {
        "role": "web developer",
        "question": "Tell me about your experience with web development."
    }
    response = requests.post(url, json=payload)
    print("Generate Answer Response:", response.json())

def test_analyze_answer():
    url = f"{BASE_URL}/analyze_answer"
    payload = {
        "role": "web developer",
        "question": "Tell me about your experience with web development.",
        "user_answer": "I have worked on several web projects using React and Django."
    }
    response = requests.post(url, json=payload)
    print("Analyze Answer Response:", response.json())

if __name__ == "__main__":
    test_generate_answer()
    test_analyze_answer()
