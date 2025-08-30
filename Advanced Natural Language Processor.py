import re
from typing import List, Dict, Tuple
from collections import Counter, defaultdict
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

class AdvancedNLP:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()
        
    def preprocess_text(self, text: str) -> str:
        # Remove special characters and digits
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Convert to lowercase
        text = text.lower()
        # Tokenize
        tokens = word_tokenize(text)
        # Remove stopwords and stem
        tokens = [self.stemmer.stem(token) for token in tokens if token not in self.stop_words]
        return ' '.join(tokens)
    
    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        doc = self.nlp(text)
        entities = defaultdict(list)
        for ent in doc.ents:
            entities[ent.label_].append(ent.text)
        return dict(entities)
    
    def sentiment_analysis(self, text: str) -> float:
        # Simple sentiment analysis using word scores
        positive_words = {'good', 'great', 'excellent', 'amazing', 'wonderful'}
        negative_words = {'bad', 'terrible', 'awful', 'horrible', 'poor'}
        
        tokens = word_tokenize(text.lower())
        positive_count = sum(1 for token in tokens if token in positive_words)
        negative_count = sum(1 for token in tokens if token in negative_words)
        
        if positive_count + negative_count == 0:
            return 0
        return (positive_count - negative_count) / (positive_count + negative_count)
    
    def text_similarity(self, text1: str, text2: str) -> float:
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([text1, text2])
        return cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    
    def keyword_extraction(self, text: str, top_n: int = 10) -> List[Tuple[str, float]]:
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform([text])
        feature_names = vectorizer.get_feature_names_out()
        
        scores = zip(feature_names, tfidf_matrix.toarray()[0])
        sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
        return sorted_scores[:top_n]
    
    def summarize_text(self, text: str, num_sentences: int = 3) -> str:
        sentences = sent_tokenize(text)
        if len(sentences) <= num_sentences:
            return text
        
        # Score sentences based on word frequency
        words = word_tokenize(text.lower())
        word_freq = Counter(words)
        max_freq = max(word_freq.values()) if word_freq else 1
        
        sentence_scores = {}
        for i, sentence in enumerate(sentences):
            sentence_words = word_tokenize(sentence.lower())
            score = sum(word_freq[word] for word in sentence_words) / len(sentence_words)
            sentence_scores[i] = score / max_freq
        
        # Select top sentences
        top_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)[:num_sentences]
        top_sentences.sort(key=lambda x: x[0])  # Maintain original order
        
        return ' '.join(sentences[i] for i, _ in top_sentences)
    
    def named_entity_recognition(self, text: str) -> List[Tuple[str, str]]:
        doc = self.nlp(text)
        return [(ent.text, ent.label_) for ent in doc.ents]
    
    def dependency_parsing(self, text: str) -> List[Tuple[str, str, str]]:
        doc = self.nlp(text)
        return [(token.text, token.dep_, token.head.text) for token in doc]

# Example usage
nlp = AdvancedNLP()
text = "Apple Inc. is planning to open a new store in New York City next month."
print("Entities:", nlp.extract_entities(text))
print("Sentiment:", nlp.sentiment_analysis(text))
print("Keywords:", nlp.keyword_extraction(text))
