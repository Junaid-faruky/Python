import spacy
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from fuzzywuzzy import fuzz

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\W+', ' ', text)
    return text.lower()

def extract_skills(text):
    doc = nlp(text)
    skills = [token.text for token in doc if token.pos_ in ['NOUN', 'PROPN']]
    return list(set(skills))

def similarity_score(resume_text, job_desc):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_desc])
    return (vectors * vectors.T).A[0,1] * 100  # percentage
