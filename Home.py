import streamlit as st
from pathlib import Path
import os
import streamlit.components.v1 as components

# https://developer.chrome.com/docs/lighthouse/seo/meta-description/?utm_source=lighthouse&utm_medium=lr
# https://developer.mozilla.org/en-US/docs/Web/Manifest

st.set_page_config(
    page_title="Nguyen Minh Duc - Portfolio Website",
    page_icon=":page_facing_up:",
    layout="centered",
    # initial_sidebar_state="collapsed",
    # menu_items=None
)
st._config.set_option("theme.base", "dark")

# # Include Google Analytics tracking code (doesnt work)
# with open("analytics.html", "r") as f:
#     html_code = f.read()
#     components.html(html_code, height=0)

# components.iframe('analytics.html', height=1, scrolling=False)
# components.html(r'analytics.html')

metadata = """
<h1 style="display: none;">Nguyen Minh Duc | Nguyen Minh Duc</h1>
<p style="display: none;">Welcome to the website of Nguyen Minh Duc. This is Duc online portfolio and digital resume website</p>"""
st.markdown(metadata, unsafe_allow_html=True)


# Potential work-around to fixing Google Search Console code integration issue (https://github.com/streamlit/streamlit/issues/6567#issuecomment-2143512104)
# index = Path(st.__file__).parent / "static" / "index.html"
# # os.chmod(index, 0o777)
# html = index.read_text()
# st.write(html)
# metadata = """<meta name='url' content='https://minhduc/streamlit.app'>
# <meta name="author" content="Nguyen Minh Duc, nguyenminhduc890@gmail.com">
# <meta name='copyright' content='Nguyen Minh Duc, nguyenminhduc890@gmail.com'>
# <meta name="application-name" content="Nguyen Minh Duc - Portfolio Website">
# <meta name="google-site-verification" content="OP3yEmLoPHFKz6nzUVU_aWuso0ZWhv2MYBNlE0VQb0k" />
# <meta name="description" content="Welcome to Nguyen Minh Duc's Digital/Online Resume, and portfolio website">

# # Replace the target string
# if metadata not in html:
#   html = html.replace("<head>", "<head>" + metadata)
#   # Write the file out again
#   with open(index, "w+") as f:
#     f.write(html)
#     print("Inserted metadata into:", index)
# else:
#   print("Metadata not inserted: Already exists")


def main():
    # Dark mode
    with st.sidebar:
        if st.toggle("Dark Mode", value=True) is False:
            st._config.set_option(f"theme.base", "light")
        else:
            st._config.set_option(f"theme.base", "dark")

        # Refresh button
        if st.button(
            "Refresh",
            help="Refresh page if something isn't updating accordingly",
            use_container_width=True,
        ):
            st.rerun()

        # Clear button
        if st.button(
            "Clear Session",
            help="Clears session, cache, and cookie data",
            use_container_width=True,
        ):
            st.cache_data.clear()
            st.session_state.clear()
            st.cache_resource.clear()
            st.rerun()
        st.markdown(
            "Copyright ©️ 2024 :blue[Nguyen Minh Duc.]<br>All rights reserved.",
            unsafe_allow_html=True,
        )

    row0 = st.columns([2, 4], gap="medium")

    # Hero Section
    with row0[0]:
        st.image("./assets/Minh-Duc.jpg", width=230)

    with row0[1]:
        st.header("Nguyen Minh Duc", anchor=False)
        st.write(
            """
             :blue[Student]
              """
        )
        with open("./assets/Minh-Duc_CV.pdf", "rb") as file:
            pdf_file = file.read()
        st.download_button(
            label="Download my :blue[resume]",
            data=pdf_file,
            file_name="resume",
            mime="application/pdf"
        )
        # row1 = st.columns([0.8, 1, 1.05, 0.9])
        row1 = st.columns([1, 1, 1])
        row1[0].link_button(
            ":orange[@ Email]",
            url="mailto:nguyenminhduc890@gmail.com",
            help="nguyenminhduc890@gmail.com",
            use_container_width=True,
        )
        # row1[1].link_button(":red[:globe_with_meridians: Website]", url="https://mindutch03.streamlit.io", help="alisterbaroi.streamlit.io", use_container_width=True)
        row1[1].link_button(
            ":blue-background[in] :blue[LinkedIn]",
            url="https://www.linkedin.com/in/minhduc030303",
            help="linkedin.com/in/minhduc030303",
            use_container_width=True,
        )
        row1[2].link_button(
            ":computer: :green[GitHub]",
            url="https://github.com/MinDutch03",
            help="github.com/MinDutch03",
            use_container_width=True,
        )

    st.markdown("<style>hr{margin: 0;}</style>", unsafe_allow_html=True)
    st.divider()

    # Summary Section
    st.subheader("Summary", anchor=False)
    st.markdown(
        """
  - 🏆 A final-year student in Computer Science at Vietnamese German University (Vietnam),
  - 👔 Friendly, studios, punctilious,
  - 🔥 Majored in Data, Machine/Deep Learning
  """
    )

    # Skills Section
    st.subheader("Skills", anchor=False)
    with st.expander("Programming Languages"):
        st.multiselect(
            "Programming Languages",
            [
                "Python",
                "JavaScript",
                "Git",
                "YAML",
                "SQL",
                "C++",
                "Java",
                "Bash",
                "PowerShell",
                "HTML",
                "CSS"
            ],
            [
                "Python",
                "JavaScript",
                "Git",
                "YAML",
                "SQL",
                "C++",
                "Java",
                "Bash",
                "PowerShell",
                "HTML",
                "CSS"
            ],
            disabled=False,
            label_visibility="collapsed",
        )

    with st.expander("Frameworks & Libraries"):
        st.multiselect(
            "Frameworks & Libraries",
            [
                "Restful API",
                "Streamlit",
                "Docker",
                "Django",
                "Seaborn",
                "Keras",
                "Anaconda",
                "TensoFlow",
                "Scikit-learn",
                "Matplotlib",
                "React",
                "Langchain",
                "OpenAI API",
                "Google API"
            ],
            [
                "Restful API",
                "Streamlit",
                "Docker",
                "Django",
                "Seaborn",
                "Keras",
                "Anaconda",
                "TensoFlow",
                "Scikit-learn",
                "Matplotlib",
                "React",
                "Langchain",
                "OpenAI API",
                "Google API"
            ],
            disabled=False,
            label_visibility="collapsed",
        )

    with st.expander("Platforms & Tools"):
        st.multiselect(
            "Platforms & Tools",
            [
                "Google Cloud Platform",
                "GitHub",
                "Gitlab",
                "GitHub Actions",
                "Docker",
                "Linux",
                "MySQL",
                "PostgreSQL",
                "MySQL",
                "MongoDB",
                "Figma",
                "Jupyter Notebooks",
                "Google Colab",
                "Microsoft Office",
                "Google Workspace"
            ],
            [
                "Google Cloud Platform",
                "GitHub",
                "Gitlab",
                "GitHub Actions",
                "Docker",
                "Linux",
                "MySQL",
                "PostgreSQL",
                "MySQL",
                "MongoDB",
                "Figma",
                "Jupyter Notebooks",
                "Google Colab",
                "Microsoft Office",
                "Google Workspace"
            ],
            disabled=False,
            label_visibility="collapsed",
        )

    with st.expander("Technology Concepts"):
        st.multiselect(
            "Technology Concepts",
            [
                "Microservices",
                "AI",
                "Backend",
                "Data Analysis",
                "Data Science",
                "Machine Learning",
                "Software Architecture",
                "Prompt Enfineering"
            ],
            [
                "Microservices",
                "AI",
                "Backend",
                "Data Analysis",
                "Data Science",
                "Machine Learning",
                "Software Architecture",
                "Prompt Enfineering"
            ],
            disabled=False,
            label_visibility="collapsed",
        )

    with st.expander("Soft skills"):
        st.multiselect(
            "List of Soft Skills",
            [
                "Adaptability",
                "Collaboration",
                "Confidence",
                "Creativity",
                "Critical Thinking",
                "Emotional Intelligence",
                "Empathy",
                "Organization",
                "Problem Solving",
                "Presentation",
                "Teamwork"
            ],
            [
                "Adaptability",
                "Collaboration",
                "Confidence",
                "Creativity",
                "Critical Thinking",
                "Emotional Intelligence",
                "Empathy",
                "Organization",
                "Problem Solving",
                "Presentation",
                "Teamwork"
            ],
            disabled=False,
            label_visibility="collapsed",
        )

    # Experience Section
    st.subheader("Experience", anchor=False)
    with st.expander("Teky :gray[(*Jul 2023 - Sep 2023*)]"):
        with st.container(border=True):
            jobcol = st.columns([1.5, 1.5, 1])
            jobcol[0].write(":blue[Teaching Assistant]")
            jobcol[1].write(":grey[Ho Chi Minh City, Vietnam (Remote)]")
            jobcol[2].write(":gray[*Jul 2023 - Sep 2023*]")
            st.write(
                """
                - Support teacher to teach secondary students about web development.
                - Language: Python
               """
            )

    st.markdown(
        "To see the full list of my work experience (from LinkedIn), [click here](https://www.linkedin.com/in/minhduc030303/details/experience/) ➚",
        unsafe_allow_html=True,
    )

    # Education Section
    st.subheader("Education", anchor=False)
    with st.expander(
        "Bachelor of Computer Science :gray[(*Oct 2021 - Aug 2023*)]"
    ):
        with st.container(border=True):
            jobcol = st.columns([1.5, 1.5, 1])
            jobcol[0].write(":blue[Bachelor of Computer Science]")
            jobcol[1].write(":grey[Vietnamese German University - Vietnam]")
            jobcol[2].write(":grey[*Oct 2021 - Aug 2023*]")
            st.write(
                """
              - Major/specilization in :green[Artificial Intelligence] (AI)
              - GPA: :green[2.0/4.0] (German Scale)
              - Honors and Awards: :green[DAAD scholarship], :green[Merit-based scholarship]
                 """
            )

        with st.container(border=True):
            jobcol = st.columns([1.5, 1.5, 1])
            jobcol[0].write(":blue[Bachelor of Computer Science (Double Degree)]")
            jobcol[1].write(
                ":grey[Frankfurt University of Applied Sciences (FRA UAS) - Frankfurt, Germany]"
            )
            jobcol[2].write(":grey[*Sep 2023 - Feb 2024*]")
            st.write(
                """
              - Double degree program with Vietnamese German University
              - Honors and Awards: :green[Cloudfight] Coding Contest, :green[Frankfurt UAS Contest_Herbst Programming Day 2023]
               """
            )
    with st.expander("High School :gray[(*Sep 2018 - May 2021*)]"):
        with st.container(border=True):
            jobcol = st.columns([1.5, 1.5, 1])
            jobcol[0].write(":blue[High School Diploma]")
            jobcol[1].write(":grey[High School for the Gifted - Ho Chi Minh, Vietnam]")
            jobcol[2].write(":grey[*Sep 2018 - May 2021*]")

    st.markdown(
        "To see more details on my education (from LinkedIn), [click here](https://www.linkedin.com/in/minhduc030303/details/education/) ➚",
        unsafe_allow_html=True,
    )

    # Projects Section
    st.subheader("Projects", anchor=False)
    with st.container(border=True):
        jobcol = st.columns([2, 5, 2])
        jobcol[0].write("Library Management System")
        jobcol[1].write(
            ":gray[The online library management system project aims to streamline library operations, improve the user experience, and enhance access to library resources. It automates tasks such as book cataloging, tracking, and borrowing while offering user-friendly interfaces for staff and patrons. The system increases operational efficiency, improves accessibility, and provides a centralized platform for managing library resources.]"
        )
        jobcol[2].link_button(
            ":red[View Project ➚]",
            url="https://github.com/MinDutch03/Library-Management-System",
            use_container_width=True,
        )

    with st.container(border=True):
        jobcol = st.columns([2, 5, 2])
        jobcol[0].write("Object Detection with Yolov8")
        jobcol[1].write(
            ":gray[The Object Detection and Tracking Application integrates YOLOv8 with Streamlit, facilitating real-time detection and tracking of objects. Featuring a user-friendly interface, it accommodates tasks such as analyzing images and videos, processing webcam feeds, and handling YouTube videos. This versatile application streamlines the setup of detection tasks, delivering prompt and user-intuitive outcomes. Tailored for diverse scenarios, it presents a seamless approach to harnessing the robust capabilities of YOLOv8 for effective object detection and tracking.]"
        )
        jobcol[2].link_button(
            ":red[View Project ➚]",
            url="https://github.com/MinDutch03/Object_Detection_with_YOLOv8",
            use_container_width=True,
        )

    with st.container(border=True):
        jobcol = st.columns([2, 5, 2])
        jobcol[0].write("Credit Card Fraud Detection")
        jobcol[1].write(
            ":gray[In this project, the goal is to detect fraudulent credit card transactions using machine learning. Traditional systems relied on rules, but machine learning offers a more powerful approach. The dataset consists of 300,000 anonymized transactions, labeled as either fraudulent or not, with less than 0.1% being fraudulent. Achieving high accuracy is challenging due to the imbalance, as predicting all transactions as normal can result in over 99.9% accuracy. The best results are obtained using the SMOTE technique to address this imbalance.]"
        )
        jobcol[2].link_button(
            ":red[View Project ➚]",
            url="https://github.com/MinDutch03/credit_card_fraud_detection",
            use_container_width=True,
        )

    with st.container(border=True):
        jobcol = st.columns([2, 5, 2])
        jobcol[0].write("File-based Chatbot")
        jobcol[1].write(
            ":gray[A simple app allows users to input many files, then the bot will answer any questions from user based on provided files]"
        )
        jobcol[2].link_button(
            ":red[View Project ➚]",
            url="https://github.com/MinDutch03/file_based_chatbot",
            use_container_width=True,
        )

    proj_col = st.columns([1.25, 1])
    proj_col[0].write("To see the list of all my relevant projects in details, visit:")
    proj_col[1].page_link("pages/1_Projects.py", label=":blue[Projects Page ➚]")
    # ss = proj_col[1].markdown("[click here](/Projects) ➚")

    # Achievements Section
    st.subheader("Achievements", anchor=False)
    with st.container(border=True):
        jobcol = st.columns([2, 5, 2])
        a = {
            "award": "1st Prize Winner",
            "type": "Competition",
            "date": "11/2023",
            "from": "Frankfurt University of Applied Sciences",
            "des": "Placed 1st in the University",
            "link": "https://drive.google.com/file/d/1Wdf4b7V3MSZGLSovCHbi9PYKl_MEoPcC/view",
        }
        jobcol[0].write(a["award"])
        jobcol[1].write(
            ":gray[Out of 100 participants on :green[Frankfurt UAS Contest_Herbst Programming Day 2023], by Frankfurt UAS]"
        )
        if jobcol[2].button(
            ":red[View Details]", use_container_width=True, key="Herbst Programming Day"
        ):
            achievements(
                a["award"], a["type"], a["date"], a["from"], a["des"], a["link"]
            )

    with st.container(border=True):
        jobcol = st.columns([2, 5, 2])
        a = {
            "award": "1st Prize Winner",
            "type": "Competition",
            "date": "10/2023",
            "from": "Cloudflight",
            "des": "Placed 1st in Frankfurt area, placed 74 out of 214 participants in the field of AI in the world",
            "link": "https://drive.google.com/file/d/1aOtTPc9J1VAl85weI9qnKxoJhLCWYvuJ/view",
        }
        jobcol[0].write(a["award"])
        jobcol[1].write(
            ":gray[Out of many contestants on :green[Cloudflight Coding Contest], by Cloudflight]"
        )
        if jobcol[2].button(
            ":red[View Details]", use_container_width=True, key="Cloudflight"
        ):
            achievements(
                a["award"], a["type"], a["date"], a["from"], a["des"], a["link"]
            )

    with st.container(border=True):
        jobcol = st.columns([2, 5, 2])
        a = {
            "award": "DAAD",
            "type": "Scholarship",
            "date": "05/2023",
            "from": "Deutscher Akademischer Austauschdienst",
            "des": "received full sponsorship for tuition fees, living expenses, and transportation in Germany for 6 months",
            "link": None,
        }
        jobcol[0].write(a["award"])
        jobcol[1].write(
            ":gray[Got this :green[scholarship] for my exchange winter semester 2023 in Germany]"
        )
        if jobcol[2].button(
            ":red[View Details]", use_container_width=True, key="DAAD"
        ):
            achievements(
                a["award"], a["type"], a["date"], a["from"], a["des"], a["link"]
            )

    st.markdown(
        "To see the full list of my achievement (from LinkedIn), [click here](https://www.linkedin.com/in/minhduc030303/details/honors/) ➚",
        unsafe_allow_html=True,
    )

@st.experimental_dialog("Achievement", width="small")
def achievements(item, item2, item3, item4, item5, item6):
    st.write(
        f""":green[Award:]
                 {item}"""
    )
    details = st.columns([1, 1, 1])
    details[0].write(
        f""":green[Type:]
                     {item2}"""
    )
    details[1].write(
        f""":green[Date:]
                     {item3}"""
    )
    details[2].write(
        f""" :green[From:]
                     {item4}"""
    )
    st.write(
        f""":green[Description:]
             {item5}"""
    )
    if item6 is None:
        if st.button("Close"):
            st.rerun()
    else:
        btns_finnal = st.columns([2, 1])
        btns_finnal[0].link_button(
            "View Achievement ➚",
            url=item6,
            type="primary",
            use_container_width=True,
        )
        if btns_finnal[1].button("Close", use_container_width=True):

            st.rerun()


# def replace_in_file(filename, oldvalue, newvalue, findvalue):
#     """Replace string in a file and optionally create backup_filename."""
#    # Read in the file
#     with open(filename, "r") as f:
#        filedata = f.read()

#      # Replace the target string
#    if findvalue not in filedata:
#      filedata = filedata.replace(oldvalue, newvalue)
#       Write the file out again
#       with open(filename, "w") as f:
#          f.write(filedata)
#       print("Inserted metadata into:", filename)
#     else:
#       print("Metadata not inserted: Already exists")


if __name__ == "__main__":
    main()
