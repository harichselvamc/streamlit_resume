from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Harichselvam"
PAGE_ICON = ":wave:"
NAME = "Harichselvam"
DESCRIPTION = """
Driven and ambitious Computer Science student with a focus on AI and Data Science. Strong problem-solving and communication skills, complemented by a diverse set of projects and practical experience in Python, machine learning, and data analysis.
"""
EMAIL = "harichselvamc@gmail.com"
SOCIAL_MEDIA={
    "LinkedIn":"www.linkedin.com/in/harichselvamc",
    "GitHub":"https://github.com/harichselvamc",
    "Portfolio":"https://iamharichselvam.web.app/",
    "Twitter":"https://twitter.com/harichselvamc",
    "Medium":"https://medium.com/@harichselvamc",
}
PROJECTS = {
    
        "Language Translator | Online Internship | This Python project's goal is to translate a piece of text into another language. | 2022 ":" https://github.com/harichselvamc/LanguageTransulator  ",
        "Heart Failure Prediction | self-initiative | Python may be used to predict heart attacks by creating a predictive model based on different characteristics such as age, gender, medical history, and so on, and then using techniques like logistic regression or decision trees to forecast them.| 2022": "https://github.com/harichselvamc/HeartFailurePrediction",
        "Face Detection and Recognition Model | self-initiative | Developing a robust and accurate face detection and recognition model for real-time applications | 2023 ":"https://github.com/harichselvamc/Face_Detection_and_Recognition_Model_From_Scratch",
        "Pneumonia Detection Machine Learning Model | self-initiative | Pneumonia Detection Machine Learning Model using Google Teachable Machine for accurate and automated identification of pneumonia in medical imaging. | 2023 ":"https://github.com/harichselvamc/Pneumonia_Detection_Machine_Learning_Model",
        "Hotel Booking Analysis | Self-Initiative | This project aims to analyze hotel booking data to identify patterns and trends, enabling businesses to optimize their operations and enhance customer satisfaction.| 2023":"https://github.com/harichselvamc/Hotel_Booking_Analysis"
    
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
EDUCATION = """
Bachelor of Technology / Computer Science and Engineering with AI & Data Science
Dr MGR Educational and Research Institute
2021 – present
Chennai, India
"""

# --- EDUCATION ---
st.write('\n')
st.subheader("Education")
st.write("---")
education_lines = EDUCATION.splitlines()
for line in education_lines:
    st.write(line.strip())


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Online Internship  | CareerGrowth360 |Live language Transulator
- ✔️ Virtual Experience | TATA | Forage | Data Visualisation
- ✔️ Virtual Experience | KPMG | Forage | Data Analytics consulting
- ✔️ Virtual Experience | Accenture | Forage | Data Analytics and Visualization
- ✔️ Good understanding of statistical principles and their respective applications
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python,C & C++, Java, R programming, JavaScript,HTML & CSS,SQL,Dart
- 📊 Data Visulization: PowerBi, MS Excel, Plotly,Tableau,IBM CognosBi
- 🗄️ Databases: Postgres,MySQL
"""
)




# --- Internship HISTORY ---
st.write('\n')
st.subheader("Internship History")
st.write("---")

# --- JOB 1
st.write("🚧", "Python Intern | Career Growth 360")
st.write("11/2022")
st.write(
    """
- ► During my internship,I used Python, Steamlit, GoogleTrans Library, and I was also
familiar with personal OpenCV, PyDub, and I was studying artificial intelligence
with data science, so I was familiar with pandas, Scikit Learn, MatPlotLib, and
Seaborn-like libraries

"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
