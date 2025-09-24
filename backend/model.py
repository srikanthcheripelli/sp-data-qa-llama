from transformers import LlamaForCausalLM, LlamaTokenizer, pipeline

# Use a public Llama model to avoid gated repo issues
MODEL_PATH = "HuggingFaceH4/zephyr-7b-beta"

# Load tokenizer and model
tokenizer = LlamaTokenizer.from_pretrained(MODEL_PATH)
model = LlamaForCausalLM.from_pretrained(MODEL_PATH)

# Create text-generation pipeline
qa_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
)

def answer_question(question: str) -> str:
    result = qa_pipeline(
        question,
        max_new_tokens=200,
        do_sample=True,
        temperature=0.7
    )
    return result[0]["generated_text"]

