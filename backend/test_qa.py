from model import answer_question

questions = [
    "What is SP Dashboard?",
    "How do I calculate unplanned quantity?"
]

for q in questions:
    answer = answer_question(q)
    print(f"Q: {q}\nA: {answer}\n")

