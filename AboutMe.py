import streamlit as st

def app():



    col1,col2 = st.columns(2)
    with col1:


        st.subheader("<Yo✌️>")
        st.title("My Name Is Moksh Jain,A young devoloper")
    with col2:
        st.image("images/MokshPort.png")

    st.title("")
    st.write("My name is Moksh Jain .I am a robotics enthusiast and a passionate coder, as well as a young developer currently studying in 10th grade in India. I have created several apps and participated in many competitions, always striving to push the boundaries of my knowledge and skills. My ultimate goal is to become the best programmer in the world, and I am dedicated to achieving this through continuous learning and innovation.")

    st.title("Contact")
    st.write("For any queries pls email me at:")
    st.subheader("codermj11@gmail.com")
    st.write("My Github")
    st.subheader("https://github.com/Mokshprojects")





