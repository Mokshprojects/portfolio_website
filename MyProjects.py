import streamlit as st

def app():
    st.title("My projects")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.subheader("Face Mesh using cv")
        st.image("images/download.jpeg")
        st.subheader("Smart home")
        st.image("images/home.jpeg")




    with col2:
        st.subheader("Rock Paper Scissors")

        st.image("images/download (1).png")
        st.subheader("Smart irrigation system")

        st.image("images/download (1).jpeg")





    with col3:
        st.subheader("Attendence System")

        st.image("images/download (2).png")
        st.subheader("Ai recipe generator")
        st.image("images/ai.jpeg")

    st.title("Contact")
    st.write("For any queries pls email me at:")
    st.subheader("codermj11@gmail.com")
    st.write("My Github")

    st.subheader("https://github.com/Mokshprojects")




