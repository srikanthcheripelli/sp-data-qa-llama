# test_qa.py
from model import answer_question, add_qa_pair

# Add a QA pair
add_qa_pair("What is SP?", "SP stands for Service Provider.")

# Test answering
print(answer_question("What is SP?"))
print(answer_question("Explain the AI model."))

