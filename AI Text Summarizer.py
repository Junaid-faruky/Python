from transformers import pipeline

summarizer = pipeline("summarization")
text = """
Python is a high-level, interpreted programming language...
"""
summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
print(summary[0]['summary_text'])
