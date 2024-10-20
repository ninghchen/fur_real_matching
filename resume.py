import base64
import streamlit as st
from sentence_transformers import SentenceTransformer
from summarizer import Summarizer
from transformers import AutoModel, AutoTokenizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

# ------------------------page configuration------------------
st.set_page_config(
    page_title="Fur Real",  # Title of the browser tab
    page_icon="DoggoLogo.png",  # Icon for the browser tab
    layout="wide"
)

# ---------------------------page theming----------------------

page_bg_color = """
    <style>
    .stApp {
        background-color: #efd3c4; 
    }

    textarea {
	color: #57423b;
	background-color: #fffffe;
    </style>
    """
st.markdown(page_bg_color, unsafe_allow_html=True)

# ---------------------------setup title----------------------
def get_image(image_path):
    with open(image_path, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode()

image_1_url = get_image("DoggoLogo.png")  
image_2_url = get_image("shiba.png") 
title = "Fur Real Match"

st.markdown(f"""
    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 4px solid #163a84; padding: 10px;">
        <img src="data:image/png;base64, {image_1_url}" alt="Logo 1" style="height: 100px;">
        <h1 style="text-align: center; color:#163a84; font-size:64px; font-family: monospace; text-shadow: 5px 5px #e9b9a5; flex-grow: 1;">{title}</h1>
        <img src="data:image/png;base64, {image_2_url}" alt="Logo 2" style="height: 130px;">
    </div>
    """, unsafe_allow_html=True)

# ----------------------------------Cache Global Variables-------------
@st.cache_resource
def get_summarizer():
    """Create a summarizer to split a paragrah into semantic sentences"""
    model = AutoModel.from_pretrained('sentence-transformers/all-mpnet-base-v2')
    tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/all-mpnet-base-v2')
    return Summarizer(custom_model=model, custom_tokenizer=tokenizer)

@st.cache_resource
def get_model():
    """Load a model to create embedding vector for a sentence"""
    return SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

summarizer = get_summarizer()
model = get_model()

# -------------------------------Utilities-------------------------
def get_sentences(job_description, resume):
    job_sentences = summarizer.sentence_handler(job_description)
    resume_sentences = summarizer.sentence_handler(resume)

    return job_sentences, resume_sentences

def get_similarity_max(job_sentences, resume_sentences):
    js_embeddings = model.encode(job_sentences)
    rs_embeddings = model.encode(resume_sentences)

    rows = len(js_embeddings)
    columns = len(rs_embeddings)

    similarities = np.zeros((rows, columns))

    for js_index, js in enumerate(js_embeddings):
        for rs_index, rs in enumerate(rs_embeddings):
            similarity = cosine_similarity(js.reshape(1, -1), rs.reshape(1, -1))
            similarities[js_index][rs_index] = similarity[0][0]

    return similarities

def get_similarity_score(similarities):
    return np.max(similarities, axis = 1).mean()

def display_score(score):
    st.markdown(f"""<div style = "color: #57423b; font-size:40px; font-weight:bold; font-family: monospace; text-align: center; background-color: #ebb99d">Match Score: {score}%</div>""", unsafe_allow_html=True)

def display_report(similarities, job_sentences, resume_sentences):
    rows = len(job_sentences)

    for row in range(rows):
        col = np.argmax(similarities[row])
        st.write('----------------------')
        st.write('Score: ', round(similarities[row][col]*100, 2), '%')
        st.html(
            f"<p style = 'background-color:#fffffe'><span style='color:FloralWhite'>Job Requirement: </span>{job_sentences[row]}</p>"
)
        st.html(
            f"<p style = 'background-color:#fffffe'><span style='color:FloralWhite'>Best Match in Resume: </span>{resume_sentences[col]}</p>"
)
        #st.write(job_sentences[row])
        #st.write(resume_sentences[col])

# ---------------------------------Content---------------------------
job_description = st.text_area('Job Description:', 'Type here ...', height = 150)
resume = st.text_area('Resume:', 'Type here ...', height = 150)

if len(job_description) < 20 or len(resume) < 20:
    similarity_score = 0
    display_score(similarity_score)
else:
    job_sentences, resume_sentences = get_sentences(job_description, resume)
    similarities = get_similarity_max(job_sentences, resume_sentences)
    similarity_score = get_similarity_score(similarities)
    display_score(round(similarity_score*100, 2))
    display_report(similarities, job_sentences, resume_sentences)
