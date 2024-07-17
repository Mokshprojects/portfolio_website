import streamlit as st

from streamlit_option_menu import option_menu
import os

import AboutMe,MySkills,MyAskBot,Gallery,MyProjects


st.set_page_config(
    page_title="My Portfolio Website",
)

st.markdown(
    """
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src=f"https://www.googletagmanager.com/gtag/js?id={os.getenv('analytics_tag')}"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', os.getenv('analytics_tag'));
        </script>
    """, unsafe_allow_html=True)
print(os.getenv('analytics_tag'))


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        st.logo("images/loogo.png")
        # app = st.sidebar(
        with st.sidebar:
            app = option_menu(
                menu_title='My Portfolio Website',
                options=['About Me', 'My Skills', 'My Ask Bot','My Setup','My Projects'],
                icons=['info-circle-fill',  'trophy-fill', 'chat-fill','camera-fill','book-fill'],
                menu_icon="cast",
                default_index=1,


                styles={
                    "container": {"padding": "0!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "#02ab21"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }


            )

        if app == "About Me":
            AboutMe.app()
        if app == "My Skills":
            MySkills.app()
        if app == "My Ask Bot":
            MyAskBot.app()
        if app == "My Projects":
            MyProjects.app()
        if app == "My Setup":
            Gallery.app()


    run()
