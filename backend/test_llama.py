# test_llama.py
from model import answer_question

questions = [
    "What is the capital of France?",
    "Explain the process of photosynthesis in simple terms."
]

for q in questions:
    ans = answer_question(q)
    print(f"Q: {q}\nA: {ans}\n")

