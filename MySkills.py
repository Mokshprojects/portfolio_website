import streamlit as st

def app():

    st.title("My Skills")

    css_style = """
    <style>
    /* Change the color of the slider track */
    div[data-baseweb="slider"] > div > div {
        background: #40E0D0 !important; /* Turquoise color for the slider track */
    }

    /* Change the color of the slider thumb */
    div[data-baseweb="slider"] > div > div > div {
        background: #ff69b4 !important; /* Hot pink color for the slider thumb */
        border: 2px solid #ffffff !important; /* White border for better visibility */
    }

    /* Change the color of the slider values */
    div[data-baseweb="slider"] > div > div > div > div > div {
        color: #ff69b4 !important; /* Hot pink color for the slider values */
    }
    </style>
    """

    # Inject the CSS style into the Streamlit app
    st.markdown(css_style, unsafe_allow_html=True)
    st.slider("Programming",0,100,80)
    st.slider("Robotics",0,100,85)
    st.slider("Mechanical",0,100,65)
    st.subheader("")
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Won Motivation Award In Ftc competition")
        st.write(" - Ftc - First tech challenge")

        st.write("- Was the head of the programming team")
        st.write("- Came in 8th position in Ftc comp")
        st.write("- created several apps")
        st.write("- Developing projects in python since 2 years")
        st.write("- Doing Robotics since 5 years")


    with col2:
        st.title("")

        st.image("images/Moti.png")

    col1, col2 = st.columns(2)
    with col1:
        st.title("")
        st.subheader("My Youtube channel")
        st.write("- I create anime and coding content")
        st.write("- Over 7k views in all my videos")



    with col2:
        st.video("https://youtu.be/4WLXntOGxcs?si=YjhG0JAMqJgFWZSu")

    st.title("Contact")
    st.write("For any queries pls email me at:")
    st.subheader("codermj11@gmail.com")



