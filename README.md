
# 📄 Resume Analyzer

A Flask + spaCy web application that analyzes how well a resume matches a job description using natural language processing (NLP). Get a match percentage and discover overlapping keywords.

![screenshot](docs/demo.png) <!-- Optional: add screenshot later -->

---

## 🚀 Features

- Upload or paste resume and job description
- Extracts and compares relevant keywords
- Calculates a match percentage using NLP + cosine similarity
- Responsive, clean UI for desktop and mobile

---

## 🛠 Tech Stack

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [spaCy](https://spacy.io/)
- [scikit-learn](https://scikit-learn.org/)
- HTML/CSS (vanilla + grid layout)

---

## 📦 Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/resume-analyzer.git
   cd resume-analyzer
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

4. **Run the app**
   ```bash
   flask run
   ```

5. **Visit in browser**
   ```
   http://127.0.0.1:5000
   ```

---

## 📁 Project Structure

```
resume-analyzer/
├── app.py
├── utils.py
├── requirements.txt
├── .flaskenv
├── .gitignore
├── templates/
│   └── index.html
├── static/
│   └── styles.css
└── README.md
```

---

## ✅ To-Do / Roadmap

- [ ] REST API endpoint for automation
- [ ] Word cloud visualization
- [ ] Section-wise analysis (Skills / Education / Experience)
- [ ] Export report as CSV or PDF
- [ ] Deploy to Render / PythonAnywhere

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

- Built with ❤️ using [spaCy](https://spacy.io/)
- Inspired by job seekers and recruiters wanting to bridge the skill gap