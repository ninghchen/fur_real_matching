# Fur Real Match
girls hoo hack uva 2024 hackathon

## Website URL:
Welcome! The website app is hosted on Streamlit Community Cloud.
You can access it [here](https://furrealmatching-ninghchen.streamlit.app/).

If that does not work you can also copy and paste this url: https://furrealmatching-ninghchen.streamlit.app/

---
## Citations
**Languages:**
- Python
- HTML
- CSS

**Frameworks:**
- Streamlit
- Scikit Learn

**Platforms:**
- Github
- Streamlit Community Cloud

**Cloud Services:**
- Hugging Face Transformer Model [Documentation](https://huggingface.co/docs/transformers/en/index)

**Libraries:**
- Pandas
- Numpy
- Base 64 Python

**Other:**
- Canva
  
---
## Prize Tracks
- Best Beginner
- Best Overall
- Best Life Hacks Related
- Best Female Empowerment



## Inspiration
I [Hannah] applying to internships right now, but I feel like I'm getting rejected from positions even though I meet all the qualifications. One key issue is that I have C++ and Java on my resume, but job descriptions often mention 'Object-Oriented Programming' (OOP). I assumed employers would recognize that C++ implies OOP, but I later learned that the first round of applications is screened based on specific keywords. So, I wanted to create a keyword matcher to see how likely I am to make it past that first round and find ways to boost my chances.

## What it does
Our app helps users match their resumes to job descriptions by comparing the semantic similarity between the two.
When applying for jobs or internships, HR personnel often focus on specific keywords to assess candidates, as they may not fully understand the technical aspects of the role. This leads to many qualified applicants being overlooked due to missing keywords that reflect skills they already possess.
So, to increase the chance to land a job our app uses a similarity model to compare the semantic meaning of keywords in your resume with those in the job description, giving you a clear picture of how well you 'match' the role. 

1. Enter Job Description and Resume by pasting them into the two text boxes.

2. The program:
- The app breaks both the job description and your resume into sentences then uses a model to understand the meaning of the sentences.
- It compares them to see how well the skills and experiences in your resume align with what the job is asking for. Even if the wording is different, the model focuses on the meaning.

3. The app calculates a match score, giving you an overall idea of how well your resume matches the job description.

4. Detailed Report:
The app shows a detailed breakdown to help you see exactly where your resume aligns well and where it might need improvement.

## How we built it
The program builds a Streamlit app. Streamlit is a python framework that simplifies the front-end and back-end process by combining the two. 

**Overall process**
The user enters a job description and resume.
The job and resume are split into sentences.
The app calculates the similarity between each job sentence and the resume sentences.
It computes an overall similarity score and displays it.
A detailed report is generated, showing the best matching sentences between the job description and resume.

**front-end:**
The front end is integrated into the python program (integrated with the back-end) using Streamlit. Streamlit has built-in page configuration functions, but we also used the function st.markdown so that we could use typical html and css to create the front-end.

**back-end:**
1. Libraries and Imports:
Streamlit: Used to build the web app and handle user inputs.
base64: Used to encode images in base64 format to be displayed in the app.
Sentence Transformers: This includes models for embedding sentences into vector representations to capture their semantic meaning.
Summarizer: Splits the job description and resume into meaningful sentences for better analysis.
Cosine Similarity: A function from Scikit-Learn that calculates how similar two vectorized sentences are.
Pandas and Numpy: Provide data manipulation and matrix operations for calculating similarity.

2. Sentence Extraction:
The summarizer model splits job descriptions and resumes into semantically meaningful sentences
A pre-trained sentence embedding model from _hugging face_ which converts sentences into numerical vector representations. This model ignores the structure and only focuses on the semantic meaning. 

3. Similarity Calculation:
The semantic similarity is calculated between each sentence in the job description and each sentence in the resume. Then turned into a vector
Cosine similarity from sciikit learn is used to compare each pair of sentence vectors and compute similarity.
The similarities are stored in a matrix and an overall match score is computed by averaging the highest similarity scores for each sentence in the job description.

## Challenges we ran into
**We changed ideas:** Our original idea was to create a pet matcher. Since the pound doesn’t create profiles for their animals and they have a high put-down rate, we thought we could create an app that matched a person’s wants to a pet profile. However, the hugging face model I chose to use to compare text does not distinguish between similar semantic words like cat and dog. Then, we found that it works for general keywords. 

**Program bugs:** 
- We couldn’t add a button, so currently it works by clicking on the screen. 
- You also need to refresh the screen every time you want a new one
- It only works effectively with longer text


## Accomplishments that we're proud of
- The software mostly works!
- We successfully deployed a website with Github without help.
- Getting the website to look cute: So many color combinations clashed with our dog images. 


## What we learned
- How to effectively use python models. 
- How to use Streamlit: We really wanted to use certain python models but they dont integrate well with HTMl and CSS, so learning streamlit allowed us to use all three


## What's next for Fur Real Match
Expand into an app that allows users to input a profile into a public network and allow employers to automatically see match rates for each profile.  Vise versa for those looking for jobs.  This software would make it easier for both applicants and employers to optimize compatibility.  In addition, a communication system that allows for online conversations could be developed in addition to the profile system, fostering even more connections between applicants and employers.  An online face-to-face facetime system could also be implemented to streamline the interviewing process. 

