from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "D L SAI TEJA RESUME.pdf"
profile_pic = current_dir / "assets" / "Teja_profile.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | LAKSHMI SAI TEJA DHARMADA"
PAGE_ICON = "🧑‍💻"
NAME = "LAKSHMI SAI TEJA DHARMADA"
DESCRIPTION = """
Data Scientist | Data Engineer
"""
EMAIL = "dlsaiteja2822@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn : https://linkedin.com": "https://linkedin.com",
    "GitHub : https://github.com": "https://github.com",
    "Kaggle : https://www.kaggle.com/saitejadharmada": "https://www.kaggle.com/saitejadharmada"
}
PROJECTS = {
    """🏆 Design and Fabrication of AI based EV - Design and Fabrication of Artificial Intelligence based Electric Vehicle. Designing and Fabricating an Electric Vehicle which will drive semi autonomously with minimum human interface.
                                Designing structure of the Vehicle for efficient load carrying.
                                Positioning mechanical, electrical and electronic components maintaining load balance.
                                Installed Raspberry Pi 4, relay circuit and ultrasonic sensors for detecting obstacles and navigate passengers to go in safe direction.""":'.',
    """🏆 Personal Voice Assistant - virtual assistant that can do various things such as tell the time, play music on YouTube, send messages on WhatsApp, search the web, and open applications on your computer, among others.
                                It uses various APIs such as SpeechRecognition, Pyttsx3, PyWhatKit, Wikipedia, and OpenAI.
                                it will ask for a password. If the password is correct, it will start listening for commands. You can ask it to perform various tasks, and it will respond accordingly.""":'.',
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
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- QUALIFICATIONS ---
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Qulifications")
st.write(
    """
- \t\t✔️ XII : Sri Chaitanya Juniour Collage \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tCGPA : 9.1, YOP : 2018
- \t\t✔️ UG : Bonam Venkata Chalamayya Institution of Technology and Science Amalapuram - JNTUK\t\t\t\t\tCGPA : 7.04, YOP : 2022.
- \t\t✔️ PGP :Post Graduation Program in Computational Datascience - Upgrade INSOFE\t\t\t\t\t\t\t\tDuration : May 2022 - April 2023
- Excellent team-player and displaying strong sense of initiative on tasks
- Strong Communication and presentation skills
"""
)


# --- SKILLS ---
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
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


# --- Compititions---
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Compititions")
st.write("---")

# --- JOB 1
st.write("🚧", """**[Binary Classification with a Tabular Credit Card Fraud Dataset]** | Kaggle competition – Playground Series 3 Episode 4""")
st.write("Rank: 441th of 641 | Top 68%")
st.write(
    """
- ► Purpose: To predict whether a credit card transaction is fraudulent or not
- ► Handled severely imbalanced data and built various supervised machine learning classification algorithms
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", """[Ordinal Regression with a Tabular Wine Quality Dataset] | Kaggle competition – Playground Series 3 Episode 5""")
st.write("Rank: 255th of 901 | Top 29%")
st.write(
    """
- ► Purpose: To predict the Wine Quality
- ► Conducted data cleaning and pre-processing along with visualization
- ► Feature Engineering of chemical properties to reduce dimensions of data
- ► Constructed various machine learning classification models
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", """[Regression with a Tabular Paris Housing Price Dataset] | Kaggle competition – Playground Series 3 Episode 6""")
st.write("Rank: 40th of 703 | Top 6%")
st.write(
    """
- ► Purpose: To predict the price of houses in Paris
- ► Conducted data cleaning and pre-processing along with visualization
- ► Analyzed various attributes (house features) and their relation with target (house price)
- ► Constructed various machine learning regression models
"""
)




# --- Projects & Accomplishments ---
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.subheader("Projects & Accomplishments")
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