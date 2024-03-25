from pathlib import Path
import streamlit as st
from PIL import Image


def resume():

    # --- PATH SETTINGS ---
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    css_file = current_dir / "styles" / "main.css"
    resume_file = current_dir / "assets" / "CV.pdf"
    profile_pic = current_dir / "assets" / "profile-pic.png"


    # --- GENERAL SETTINGS ---
    PAGE_TITLE = "BOUGHANMI Youssef"
    PAGE_ICON = ":shark:"
    NAME = "BOUGHANMI Youssef"

    DESCRIPTION = """
    Full Stack Data Science | Python | SQL | ML Engineer | 42 Student
    """

    EMAIL = "boughanmi-youssef1@outlook.fr"
    SOCIAL_MEDIA = {
        "LinkedIn": "https://www.linkedin.com/in/youssef-boughanmi/",
        "GitHub": "https://github.com/YoussefBOUGHANMI",
        "Youtube": "https://www.youtube.com/@MyDataMinds"
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
        st.write("📍", "Nice, FRANCE")
        st.write("📫", EMAIL)


    # --- SOCIAL LINKS ---
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")


    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.subheader("Experience & Qulifications")
    st.write(
        """
    - ✔️ 3 Years expereince extracting actionable insights from data
    - ✔️ Strong hands on experience and knowledge in Python and Hadoop system
    - ✔️ Good understanding of statistical principles and their respective applications
    - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
    """
    )

    
    # --- SKILLS ---
    st.write('\n')
    st.subheader("Hard Skills")
    st.write(
        """
    - 👩‍💻 Programming languages: Python, R, SQL, C/C++, Bash
    - 📁 Infrastructure management: Git, Docker, Kubernetes
    - 🤖 AI/ML Libraries: Pandas, NumPy, Scikit-learn, TensorFlow, Keras, PySpark
    - 📊 Data visualization: Matplotlib, Seaborn, Excel, streamlit
    - 🗄️Databases: MySQL, Hive, SAS
    - 📚 Machine learning techniques: regression, classification, clustering,
    decision trees, neural networks, etc.
    """
    )


    # --- WORK HISTORY ---
    st.write('\n')
    st.subheader("Work History")
    st.write("---")

    # --- JOB 1
    st.write("🚧", "**Data Scientist | Crédit Agricole | Permanent contract**")
    st.write("03/2021 - Present")
    st.write(
        """
    - ► Detection of Fraudulent Checks using Python, Hive, and PySpark.
    - ► Early Identification of High-Risk Clients with Python, Hive, and PySpark.
    - ► Development of a Lead Management Algorithm for Prioritization and Allocation, utilizing Python and SQL.
    - ► Calculation of Appreciation Scores to Enhance Marketing Campaign Performance, implemented in Python and SQL.
    - ► Customization of Banking Card Limits through an Algorithm, employing Python, SQL, and Oozie.
    - ► Generation of the Next Best Offer, providing a tailored recommendation for the most suitable offer for each client, with Python, Hive, and PySpark.
    - ► Development of a Kafka Consumer Application for Real-Time Data Flow Processing, using Python and Kafka.
    """
    )

    # --- JOB 2
    st.write('\n')
    st.write("🚧", "**Data Scientist | Amadeus | End of studies' project**")
    st.write("09/2020 - 03/2021")
    st.write(
        """
    - ► Anomaly detection using machine learning: the objective is to analyze all the data recorded in the logbook generated during the testing phases of a program, in order to automatically resolve errors that result.
    """
    )



    # --- Education ---
    st.write('\n')
    st.subheader("Education")
    st.write("---")

    # --- Education 1
    st.write("🎓", "**school 42 | Computer Science**")
    st.write("2022 - 2024")
    st.write(
        """
    - ► 42 School is a tuition-free coding education program known for its innovative, peer-to-peer, project-based learning approach. Founded in Paris by Xavier Niel, it eschews traditional teaching methods in favor of a hands-on, collaborative environment
    """)
    st.write('\n')

    # --- Education 2
    st.write("🎓", "**Côte d'Azur University | Master of Science - MS | Mathematical engineering**")
    st.write("2019 - 2021")
    st.write(
        """
    - ► The Master of Science (MS) in Mathematical Engineering is an advanced degree focusing on the application of mathematics to solve complex engineering problems, integrating analytical and computational methods.
    """)

    st.write('\n')
    # --- Education 3
    st.write("🎓", "**Côte d'Azur University | Bachelor's degree | Mathematics**")
    st.write("2015 - 2018")
    st.write(
        """
    - ► A Bachelor's degree in Mathematics is an undergraduate program that offers a foundational understanding of mathematical theories, techniques, and applications across various fields.
    """)
    return('\n')


resume()