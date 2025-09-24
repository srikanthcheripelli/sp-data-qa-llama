from transformers import LlamaForCausalLM, LlamaTokenizer
import torch
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "llama-2-7b")  # local folder

# Load tokenizer from local folder
tokenizer = LlamaTokenizer.from_pretrained(MODEL_PATH, local_files_only=True)

# Load model from local folder
device = "cuda" if torch.cuda.is_available() else "cpu"
model = LlamaForCausalLM.from_pretrained(MODEL_PATH, device_map="auto", local_files_only=True)

def answer_question(question, max_length=256):
    inputs = tokenizer(question, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_length,
            do_sample=True,
            temperature=0.7,
            top_p=0.9
        )
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer

