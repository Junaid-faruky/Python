# 8. HuggingFace Transformers
from transformers import pipeline
qa = pipeline("question-answering")
print(qa(question="Capital of France?", context="Paris is the capital of France."))
