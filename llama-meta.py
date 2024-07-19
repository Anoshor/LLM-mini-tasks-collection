from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(
    "baffo32/decapoda-research-llama-7B-hf",
    use_fast=False,
    legacy=False  # Set legacy to False
)
model = AutoModelForCausalLM.from_pretrained("baffo32/decapoda-research-llama-7B-hf")

# Initialize the text generation pipeline
classifier = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Generate a response
prompt = "Why is the ocean salty?"
response = classifier(prompt, max_length=150, num_return_sequences=1, do_sample=True)
print(response)