import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Nguyen Minh Duc", page_icon=":page_facing_up:", layout="centered"
)


def main():
    st.title("Projects —")
    st.markdown("<style>hr{margin: 0;}</style>", unsafe_allow_html=True)
    st.write(
        "Here are all my relevant AI/ML, Web Development, and cloud projects — Enjoy!!"
    )
    st.divider()
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
            st._config.set_option(f"theme.base", "dark")
            st.cache_data.clear()
            st.session_state.clear()
            st.cache_resource.clear()
            st.rerun()
        st.markdown(
            "Copyright ©️ 2024 :blue[Nguyen Minh Duc.]<br>All rights reserved.",
            unsafe_allow_html=True,
        )

    # Project: Library Management System
    with st.container(border=True):
        jobcol = st.columns([2, 5, 2])
        a = {
            "name": "Library Management System",
            "tech": "TypeScript, Javascript, Sequelize DB, API",
            "date": "06/2024",
            "platform": "Linux, Windows, Docker",
            "des": "This Library project the online system will offer web interfaces that allow users to search for books, view availability, and place online reservations from anywhere, at any time. It eliminates the need for physical visits to the library and provides convenient access to resources remotely. ",
            "link": "https://github.com/MinDutch03/Library-Management-System",
            "image": "./assets/Library_UI.png",
            "video": None,
        }
        jobcol[0].write(a["name"])
        jobcol[1].write(
            f":gray[The system increases operational efficiency, improves accessibility, and provides a centralized platform for managing library resources. :green[Date: {a['date']}]]"
        )
        if jobcol[2].button(":red[View Details]", use_container_width=True, key="Library"):
            project(
                a["name"],
                a["date"],
                a["tech"],
                a["platform"],
                a["des"],
                a["link"],
                a["image"],
                a["video"],
            )

    # Project: File-based Chatbot
    with st.container(border=True):
        jobcol = st.columns([2, 5, 2])
        a = {
            "name": "File-based Chatbot",
            "tech": "Python, Machine Learning, Deep Learning",
            "date": "07/2024",
            "platform": "Google Generative AI, Google Cloud Platform",
            "des": "Allow users to input many files, then the bot will answer any questions from user based on provided files.",
            "link": "https://github.com/MinDutch03/file_based_chatbot",
            "image": "./assets/file_based_chatbot.png",
            "video": None,
        }
        jobcol[0].write(a["name"])
        jobcol[1].write(
            f":gray[A website for file input, process with computer vision & LLM, & send back the answer for user's questions based on the file. :green[Date: {a['date']}]]"
        )
        if jobcol[2].button(
            ":red[View Details]", use_container_width=True, key="Chatbot"
        ):
            project(
                a["name"],
                a["date"],
                a["tech"],
                a["platform"],
                a["des"],
                a["link"],
                a["image"],
                a["video"],
            )

    # Project: Object_Detection_with_YOLOv8
    with st.container(border=True):
        jobcol = st.columns([2, 5, 2])
        a = {
            "name": "Object_Detection_with_YOLOv8",
            "tech": "Python, Machine Learning, Deep Learning",
            "date": "07/2024",
            "platform": "Streamlit",
            "des": "The Object Detection and Tracking Application integrates YOLOv8 with Streamlit, facilitating real-time detection and tracking of objects. Featuring a user-friendly interface, it accommodates tasks such as analyzing images and videos, processing webcam feeds, and handling YouTube videos. This versatile application streamlines the setup of detection tasks, delivering prompt and user-intuitive outcomes. Tailored for diverse scenarios, it presents a seamless approach to harnessing the robust capabilities of YOLOv8 for effective object detection and tracking.",
            "link": "https://github.com/MinDutch03/Object_Detection_with_YOLOv8",
            "image": "./assets/interface.png",
            "video": None,
        }
        jobcol[0].write(a["name"])
        jobcol[1].write(
            f":gray[Integrate many features such as Multi-Source Compatibility, Dynamic Model Configuration, YouTube Video URL Detection, Webcam Detection and User-Friendly Interface. :green[Date: {a['date']}]]"
        )
        if jobcol[2].button(
            ":red[View Details]", use_container_width=True, key="YOLOv8"
        ):
            project(
                a["name"],
                a["date"],
                a["tech"],
                a["platform"],
                a["des"],
                a["link"],
                a["image"],
                a["video"],
            )

    # Project: Credit Card Fraud Detection
    with st.container(border=True):
        jobcol = st.columns([2, 5, 2])
        a = {
            "name": "Credit Card Fraud Detection",
            "tech": "Python, Machine Learning, Deep Learning",
            "date": "07/2024",
            "platform": "Jupyter Notebook",
            "des": "The project uses a dataset of 300,000 fully anonymized transactions. Each transaction is labeled either fraudulent or not fraudulent. Note that the prevalence of fraudulent transactions is very low in the dataset—less than 0.1% of the card transactions are fraudulent. This means that a system predicting each transaction to be normal can reach an accuracy of over 99.9%  in spite not detecting any fraudulent transaction. This will necessitate adjustment techniques. The best performance is achieved using the SMOTE technique.",
            "link": "https://github.com/MinDutch03/credit_card_fraud_detection",
            "image": "./assets/fullset.png",
            "video": None,
        }
        jobcol[0].write(a["name"])
        jobcol[1].write(
            f":gray[In this project, I aim to identify fraudulent transactions with credit cards. The objective is to build a fraud detection system using machine learning techniques. Historically, such systems were rule-based, but machine learning offers powerful new ways to detect Fraudulent Credit Card transactions and compare performances. :green[Date: {a['date']}]]"
        )
        if jobcol[2].button(
            ":red[View Details]", use_container_width=True, key="Credit Card"
        ):
            project(
                a["name"],
                a["date"],
                a["tech"],
                a["platform"],
                a["des"],
                a["link"],
                a["image"],
                a["video"],
            )

    # Project: Distributed Real-time chat application
    with st.container(border=True):
        jobcol = st.columns([2, 5, 2])
        a = {
            "name": "Distributed Real-time chat application",
            "tech": "Javascript, React",
            "date": "06/2024",
            "platform": "Firebase",
            "des": "A web application for chatting among users using Firebase for Data backups and also solve the problem of Fault-tolerance, Scalability and Avalability",
            "link": "https://github.com/MinDutch03/Real_time_chat_application",
            "image": "./assets/realtime_chat.png",
            "video": None,
        }
        jobcol[0].write(a["name"])
        jobcol[1].write(
            f":gray[A web application for chatting among users. :green[Date: {a['date']}]]"
        )
        if jobcol[2].button(
            ":red[View Details]", use_container_width=True, key="Real-time"
        ):
            project(
                a["name"],
                a["date"],
                a["tech"],
                a["platform"],
                a["des"],
                a["link"],
                a["image"],
                a["video"],
            )

    # Project: Object Tracking
    with st.container(border=True):
        jobcol = st.columns([2, 5, 2])
        a = {
            "name": "Object-Tracking",
            "tech": "C++",
            "date": "03/2023",
            "platform": None,
            "des": "A simple program to Detect humans with bounding boxes",
            "link": "https://github.com/MinDutch03/Object-Tracking",
            "image": None,
            "video": "https://www.youtube.com/watch?v=APUXhyFnlAU",
        }
        jobcol[0].write(a["name"])
        jobcol[1].write(
            f":gray[A simple program to Detect humans with bounding boxes.  :green[Date: {a['date']}]]"
        )
        if jobcol[2].button(
            ":red[View Details]", use_container_width=True, key="object-tracking"
        ):
            project(
                a["name"],
                a["date"],
                a["tech"],
                a["platform"],
                a["des"],
                a["link"],
                a["image"],
                a["video"],
            )

    st.markdown(
         "To see the full list of my projects, visit my [GitHub profile](https://github.com/MinDutch03) ➚",
         unsafe_allow_html=True,
    )


@st.experimental_dialog("Project Details —", width="large")
def project(item, item2, item3, item4, item5, item6, item7, item8):
    modal1 = st.columns([2, 3])
    with modal1[0]:
        if item8 is None:
            st.image(item7)
        else:
            st.video(item8)

    with modal1[1]:
        modal2 = st.columns([6, 2])
        modal2[0].write(
            f""":green[Project Name:]
                  {item}"""
        )
        modal2[1].write(
            f""" :green[Date:]
                      {item2}"""
        )
        details = st.columns([1, 1])
        details[0].write(
            f""":green[Languages/Frameworks:]
                      {item3}"""
        )
        details[1].write(
            f""":green[Platforms/Tools Used:]
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
            modalbtn = st.columns(2)
            modalbtn[0].link_button(
                "Go to Project ➚", url=item6, type="primary", use_container_width=True
            )
            if modalbtn[1].button("Close", use_container_width=True):
                st.rerun()


if __name__ == "__main__":
    main()
