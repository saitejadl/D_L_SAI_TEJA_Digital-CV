from pathlib import Path
import streamlit as st
from PIL import Image
import json
import requests
from streamlit_lottie import st_lottie

url1 = requests.get("https://lottie.host/ab8c54f3-73f2-474e-8f68-39b61d23773e/59pKiMFRkL.json")
url2 = requests.get("https://lottie.host/9f77b3ed-249b-4a6b-b073-62fcab040355/icvb7xsEBV.json")
url3 = requests.get("https://lottie.host/06f5e545-8301-4537-8906-a3b020124e47/0xwBQKW2an.json")
url4 = requests.get("https://lottie.host/ae7aa634-b616-4613-8171-e2ebb18641c3/Z5GYzAxlYE.json")
# url_json1 = dict()
# url_json2 = dict()
# url_json3 = dict()
if url1.status_code == 200:
    url_json1 = url1.json()
else:
    print("URL ERROR")
if url2.status_code == 200:
    url_json2 = url2.json()
else:
    print("URL ERROR")
if url3.status_code == 200:
    url_json3 = url3.json()
else:
    print("URL ERROR")
if url4.status_code == 200:
    url_json4 = url4.json()
else:
    print("URL ERROR")

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "D L Sai Teja Resume.pdf"
profile_pic = current_dir / "assets" / "Teja_profile.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | LAKSHMI SAI TEJA DHARMADA"
PAGE_ICON = "🧑‍💻"
NAME = "LAKSHMI SAI TEJA DHARMADA"
DESCRIPTION = """
Data Scientist | Machine Learning Engineer | Data Engineer
"""
EMAIL = "dlsaiteja2822@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn: http://www.linkedin.com/in/lakshmisaitejadharmada": "http://www.linkedin.com/in/lakshmisaitejadharmada",
    "GitHub: https://github.com/saitejadl": "https://github.com/saitejadl",
    "Kaggle: https://www.kaggle.com/saitejadharmada": "https://www.kaggle.com/saitejadharmada"
}
PROJECTS = {
    """🏆 Design and Fabrication of AI-Based Electric Vehicles: An Electric Vehicle (AIEV) that will drive semi-autonomously with the minimum human interface. Vehicle structure design for efficient load carry. Maintaining load balance by positioning mechanical, electrical, and electronic components. Installed a Raspberry Pi 4 Model B, a relay circuit, and ultrasonic sensors for detecting obstacles and navigating passengers in a safe direction. """:'.',
 
    """🏆 Personal Voice Assistant: A virtual assistant that can do various things such as tell the time, play music on YouTube, send messages on WhatsApp, search the web, and open applications on your computer, among others. It uses various APIs such as SpeechRecognition, Pyttsx3, PyWhatKit, Wikipedia, and OpenAI. It will prompt you for a password. If the password is correct, it will start listening for commands. You can ask it to perform various tasks, and it will respond accordingly. """:'.'
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON,layout="wide")


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="medium")
with col1:
    st.image(profile_pic, width=230,caption='D L SAI TEJA')

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns([3,2,3])#len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

anim1,anim2,anim3 = st.columns(3)
with anim1:
    st_lottie(url_json1)
with anim2:
    st_lottie(url_json2)
with anim3:
    st_lottie(url_json3)
    

# --- QUALIFICATIONS ---
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Qulifications")
st.write(
    """
- \t\t✔️ XII: Sri Chaitanya Juniour Collage \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tCGPA: 9.1, YOP: 2018
- \t\t✔️ UG: Bonam Venkata Chalamayya Institution of Technology and Science Amalapuram - JNTUK\t\t\t\t\tCGPA: 7.04, YOP: 2022.
- \t\t✔️ PGP: Post Graduation Program in Computational Datascience (upGrad INSOFE)\t\t\t\t\t\t\t\tDuration: May 2022–April 2023
- Excellent team player and displaying a strong sense of initiative on tasks
- Strong communication and presentation skills
"""
)


# --- SKILLS ---
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
skill1,skill2,skill3 = st.columns(3)
with skill1:
    st.subheader("Hard Skills")
    st.write(
        """
    -	👩‍💻Programming: Python (NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn), C, SQL
    -	📊Data Analysis: Data Cleaning, Statistical Modeling, Data Visualization 
    -	💻Machine Learning: Supervised learning, Unsupervised learning
    -	🧿Deep Learning: ANN, CNN, RNN, [CV, NLP]
    -	🪄Tools: My SQL, Git, Docker, Excel, Tableau
    -   ⚙️OS: Windows, Linux
    -   ☁️cloud services: AZURE
    """
    )
with skill2:
    st_lottie(url_json4)

# --- Compititions---
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Competitions")
st.write("---")

# --- JOB 3
st.write('\n')
st.write("🚧","[Regression with a Tabular Paris Housing Price Dataset] | Kaggle competition – Playground Series 3 Episode 6")

st.markdown("""[**:blue[Rank: 40th of 703 | Top 6%]**](https://www.kaggle.com/competitions/playground-series-s3e6/leaderboard?search=sai+teja+dharmada)""")
st.write(
    """
- ► Purpose: To predict the price of houses in Paris
- ► Conducted data cleaning and pre-processing along with visualization
- ► Analyzed various attributes (house features) and their relation with target (house price)
- ► Constructed various machine learning regression models
"""
)


# --- JOB 1
st.write("🚧", """**[Binary Classification with a Tabular Credit Card Fraud Dataset]** | Kaggle competition – Playground Series 3 Episode 4""")
st.write("[Rank: 441th of 641 | Top 68%](https://www.kaggle.com/competitions/playground-series-s3e4/leaderboard?tab=public&search=D+Lakshmi+Sai+Teja)")
st.write(
    """
- ► Purpose: To predict whether a credit card transaction is fraudulent or not
- ► Handled severely imbalanced data and built various supervised machine learning classification algorithms
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", """[Ordinal Regression with a Tabular Wine Quality Dataset] | Kaggle competition – Playground Series 3 Episode 5""")
st.write("[Rank: 255th of 901 | Top 29%](https://www.kaggle.com/competitions/playground-series-s3e5/leaderboard?search=D+Lakshmi+Sai+Teja)")
st.write(
    """
- ► Purpose: To predict the Wine Quality
- ► Conducted data cleaning and pre-processing along with visualization
- ► Feature Engineering of chemical properties to reduce dimensions of data
- ► Constructed various machine learning classification models
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Projects and Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


# --- Hobbies ---
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Hobbies and Interests")
st.write("---")
st.write("""
- Badminton 🏸
- Programming 💻
- Surfing Internet 🔎
- Gardening 🌱
    """)

 
# https://docs.google.com/presentation/d/1jrDigbMfp_wxzW7Eyu1jHRl0gkBYqv1c/edit?usp=share_link&ouid=110531620878687336760&rtpof=true&sd=true
