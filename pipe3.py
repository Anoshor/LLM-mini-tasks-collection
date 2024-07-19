from transformers import pipeline

classifier = pipeline("zero-shot-classification")

res = classifier(
    "This course is about Python",
    candidate_labels = ["education", "politics", "business"],
)

print(res)