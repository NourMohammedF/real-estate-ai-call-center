import subprocess
import json

def get_llm_response(prompt):
    """
    يستخدم Mistral 7B عبر ollama للرد على الأسئلة.
    """
    command = ["ollama", "run", "mistral", prompt]
    response = subprocess.run(command, capture_output=True, text=True)
    
    return response.stdout.strip()

if __name__ == "__main__":
    question = "ما هي أفضل عروض العقارات المتاحة؟"
    answer = get_llm_response(question)
    print("🤖 رد النموذج:", answer)
