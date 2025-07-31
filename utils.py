import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def load_nlp_model():
    return spacy.load("en_core_web_sm")

def extract_keywords(text, nlp):
    doc = nlp(text)
    return [token.lemma_.lower() for token in doc if token.is_alpha and not token.is_stop]

def compute_similarity(resume_keywords, jd_keywords):
    texts = [" ".join(resume_keywords), " ".join(jd_keywords)]
    vectorizer = CountVectorizer().fit_transform(texts)
    vectors = vectorizer.toarray()
    score = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
    matched = list(set(resume_keywords) & set(jd_keywords))
    return round(score * 100, 2), matched