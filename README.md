# Resume Analyzer

A Flask + NLP web application that compares a candidate's resume with a job description.

## Features
- Resume and JD text input
- spaCy-based keyword extraction
- Cosine similarity scoring
- Match percentage and keyword insights

## Setup Instructions
```bash
git clone <repo_url>
cd resume-analyzer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
flask run
```

Visit: http://127.0.0.1:5000/
