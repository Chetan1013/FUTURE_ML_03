import streamlit as st
import pandas as pd
import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



df = pd.read_csv("Resume.csv")


lemmatizer = WordNetLemmatizer()

stop_words = set(stopwords.words('english'))

def clean_text(text):
    
    text = text.lower()
    
    text = re.sub(r'http\S+', '', text)
    
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    
    words = text.split()
    
    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]
    
    return " ".join(words)



skills_list = [
    'python',
    'java',
    'sql',
    'machine learning',
    'deep learning',
    'power bi',
    'tableau',
    'excel',
    'aws',
    'docker',
    'tensorflow',
    'pytorch',
    'nlp',
    'react',
    'mongodb'
]



def extract_skills(text):
    
    text = text.lower()
    
    found_skills = []
    
    for skill in skills_list:
        
        if skill in text:
            found_skills.append(skill)
    
    return found_skills



df['cleaned_resume'] = df['Resume_str'].apply(clean_text)



st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)



st.title("📄 AI Resume Screening & Candidate Ranking System")

st.markdown("""
This system:
- Matches resumes with job descriptions
- Extracts candidate skills
- Calculates match scores
- Ranks candidates automatically
""")



job_description = st.text_area(
    "Paste Job Description",
    height=250
)



if st.button("Analyze Candidates"):
    
    cleaned_jd = clean_text(job_description)
    
    tfidf = TfidfVectorizer()
    
    resume_vectors = tfidf.fit_transform(
        df['cleaned_resume']
    )
    
    jd_vector = tfidf.transform(
        [cleaned_jd]
    )
    
    similarity_scores = cosine_similarity(
        jd_vector,
        resume_vectors
    )
    
    df['Match_Score'] = (
        similarity_scores[0] * 100
    )
    
    ranked_candidates = df.sort_values(
        by='Match_Score',
        ascending=False
    )
    
    st.subheader("🏆 Top Candidates")
    
    top_candidates = ranked_candidates[
        ['Category', 'Match_Score']
    ].head(10)
    
    st.dataframe(top_candidates)
    
    # Skill Analysis
    required_skills = extract_skills(cleaned_jd)
    
    top_resume = ranked_candidates.iloc[0][
        'cleaned_resume'
    ]
    
    candidate_skills = extract_skills(top_resume)
    
    missing_skills = list(
        set(required_skills) -
        set(candidate_skills)
    )
    
    st.subheader("✅ Matched Skills")
    st.write(candidate_skills)
    
    st.subheader("❌ Missing Skills")
    st.write(missing_skills)



st.subheader("💡 Business Benefits")

st.markdown("""
✅ Faster candidate shortlisting

✅ Reduced recruiter workload

✅ AI-powered resume ranking

✅ Better hiring decisions

✅ Skill gap identification
""")
