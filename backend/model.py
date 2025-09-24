from transformers import LlamaForCausalLM, LlamaTokenizer
import torch

MODEL_PATH = "path/to/llama"  # replace with your LLaMA weights folder

tokenizer = LlamaTokenizer.from_pretrained(MODEL_PATH)
model = LlamaForCausalLM.from_pretrained(MODEL_PATH, device_map="auto")

def answer_question(prompt, max_length=200):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=max_length)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

