# FUTURE_ML_03 — AI Resume Screening & Candidate Ranking System

## 📌 Project Overview

This project is developed as part of the **Future Interns Machine Learning Internship Task 3**.

The objective of this project is to build an **AI-powered Resume Screening and Candidate Ranking System** using Natural Language Processing (NLP) and Machine Learning techniques.

The system automatically:

* Reads resume text
* Extracts important skills
* Compares resumes with job descriptions
* Calculates similarity scores
* Ranks candidates based on job relevance
* Identifies missing skills

This project simulates how modern Applicant Tracking Systems (ATS) and HR-Tech platforms work.

---

# 🎯 Business Problem

Recruiters often receive hundreds of resumes for a single job opening.

Manual screening creates several challenges:

* Slow shortlisting process
* Inconsistent evaluation
* Missed qualified candidates
* Increased recruiter workload
* Difficulty identifying skill gaps

This project automates candidate screening using NLP and similarity scoring techniques to improve hiring efficiency.

---

# 🚀 Solution Overview

The system uses:

* NLP preprocessing
* Skill extraction
* TF-IDF vectorization
* Cosine similarity scoring

to automatically:
✅ Match resumes with job descriptions
✅ Rank candidates based on relevance
✅ Identify missing skills
✅ Assist recruiters in decision-making

---

# 📂 Dataset Used

Dataset: **Resume Dataset (Resume.csv)**

Dataset contains:

* Resume text data
* Multiple resume categories
* Various technical domains and skills

Dataset Features:

* Resume content in text format
* Multiple job categories
* NLP-ready structured dataset

---

# 🛠️ Technologies & Libraries Used

## Programming Language

* Python

## NLP Libraries

* NLTK
* spaCy

## Machine Learning

* TF-IDF Vectorization
* Cosine Similarity

## Visualization

* Matplotlib
* Seaborn

## Deployment

* Streamlit

---

# 📊 Project Workflow

## 1️⃣ Data Collection

Imported resume dataset containing multiple candidate profiles and technical domains.

---

## 2️⃣ Data Preprocessing

Performed:

* Missing value handling
* Duplicate removal
* Text cleaning
* Lowercasing
* Stopword removal
* Lemmatization
* Punctuation removal

---

## 3️⃣ Exploratory Data Analysis (EDA)

Analyzed:

* Resume category distribution
* Technical skill frequency
* Resume content patterns

Visualizations were created to understand resume trends and candidate skill distributions.

---

## 4️⃣ Skill Extraction

Extracted technical and professional skills from resumes using NLP-based keyword matching.

Examples:

* Python
* SQL
* Machine Learning
* Power BI
* AWS
* Docker

---

## 5️⃣ Job Description Parsing

The system processes job descriptions to identify:

* Required skills
* Important keywords
* Role-specific technologies

---

## 6️⃣ Resume Similarity Matching

Implemented:

### TF-IDF Vectorization + Cosine Similarity

to compare:

* Resume text
* Job description text

The similarity score determines how closely a candidate matches the required role.

---

## 7️⃣ Candidate Ranking System

Candidates are automatically ranked based on:

* Resume similarity score
* Skill relevance
* Job-role compatibility

Example:

| Candidate   | Match Score |
| ----------- | ----------- |
| Candidate A | 92%         |
| Candidate B | 87%         |
| Candidate C | 74%         |

---

## 8️⃣ Skill Gap Analysis

The system identifies:

* Missing skills
* Weak skill areas
* Required technologies absent in resumes

Example:

```text id="q66gq9"
Required Skills:
Python, SQL, AWS, Docker

Candidate Skills:
Python, SQL

Missing Skills:
AWS, Docker
```

---

# 📈 Key Features Implemented

✅ Resume Text Cleaning
✅ NLP-based Skill Extraction
✅ Job Description Parsing
✅ TF-IDF Vectorization
✅ Cosine Similarity Matching
✅ Resume-to-Role Scoring
✅ Candidate Ranking
✅ Skill Gap Identification
✅ Streamlit Dashboard
✅ Business Insights

---

# 📊 Visualizations Included

The project includes:

* Resume Category Distribution
* Candidate Match Score Charts
* Skill Match Analysis
* Ranking Visualization

---

# 💡 Business Insights

## Key Findings

* Automated resume screening significantly reduces recruiter workload.
* Similarity scoring helps identify top candidates quickly.
* Skill gap analysis improves hiring decision quality.
* ATS-style systems standardize candidate evaluation.

## Business Recommendations

* Use AI-based screening for faster hiring.
* Prioritize candidates with high similarity scores.
* Identify missing skills before technical interviews.
* Use skill-gap insights for candidate training recommendations.

---

# 📄 Example System Output

## Job Description

```text id="jlwmzz"
Looking for a Data Scientist with Python, SQL,
Machine Learning, AWS, and Power BI skills.
```

---

## System Output

```text id="jlwmzz2"
Candidate Match Score: 91%

Matched Skills:
Python, SQL, Machine Learning, Power BI

Missing Skills:
AWS
```

---

# 🚀 Streamlit Dashboard Features

The dashboard provides:

* Job description input
* Automatic resume analysis
* Candidate ranking table
* Match score calculation
* Skill gap analysis
* Business-friendly outputs

---

# 📷 Project Screenshots

Add screenshots here:

* Dashboard Interface
* Candidate Ranking Output
* Match Score Visualization
* Skill Gap Analysis
* Resume Distribution Charts

---

# 📁 Project Structure

```text id="jlwmzz4"
FUTURE_ML_03/
│
├── data/
│   └── Resume.csv
│
├── notebooks/
│   └── resume_screening.ipynb
│
├── dashboard/
│   └── app.py
│
├── outputs/
│   ├── rankings/
│   ├── charts/
│   └── reports/
│
├── screenshots/
│
├── README.md
├── requirements.txt
└── presentation.pptx
```

---

# ▶️ How to Run the Project

## Step 1 — Install Dependencies

```bash id="jlwmzz6"
pip install pandas numpy matplotlib seaborn scikit-learn nltk spacy streamlit
```

---

## Step 2 — Run Jupyter Notebook

```bash id="jlwmzz8"
jupyter notebook
```

Open:

```text id="jlwmzz9"
resume_screening.ipynb
```

---

## Step 3 — Run Streamlit Dashboard

```bash id="jlwmzza"
streamlit run app.py
```

---

# 📌 Future Improvements

Possible future enhancements:

* BERT-based semantic matching
* PDF resume upload support
* Deep learning resume ranking
* Recruiter recommendation engine
* Multi-language resume analysis
* Cloud deployment

---

# 🎯 Internship Task Objective Achieved

This project successfully fulfills all requirements of:

### Future Interns — Machine Learning Task 3

Including:

* Resume preprocessing
* Skill extraction
* Job description parsing
* Similarity scoring
* Candidate ranking
* Skill gap identification
* Business insights
* Interactive deployment

---

# 👨‍💻 Author

**MYLAVARAPU CHETAN SAI PAVAN KUMAR**

Machine Learning Intern — Future Interns

---

# 📬 Contact

*LinkedIn:https://www.linkedin.com/in/chetan-mylavarapu-554847336
*GitHub:https://github.com/Chetan1013

---

# ⭐ Acknowledgements

Special thanks to:

* Future Interns
* Open-source NLP community
* Kaggle Dataset Contributors
* HR-Tech AI Research Community

