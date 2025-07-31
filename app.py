from flask import Flask, request, render_template
from utils import load_nlp_model, extract_keywords, compute_similarity

app = Flask(__name__)
nlp = load_nlp_model()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        resume_text = request.form['resume']
        jd_text = request.form['job_description']

        resume_keywords = extract_keywords(resume_text, nlp)
        jd_keywords = extract_keywords(jd_text, nlp)
        match_score, matched_keywords = compute_similarity(resume_keywords, jd_keywords)

        return render_template('index.html',
                               match_score=match_score,
                               matched_keywords=matched_keywords,
                               resume_text=resume_text,
                               jd_text=jd_text)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)