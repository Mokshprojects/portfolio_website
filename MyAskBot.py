import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=api_key)


model = genai.GenerativeModel('gemini-1.5-flash')

def app():
    persona = """
            You are Moksh AI bot. You help people answer questions about your self (i.e Moksh)
            Answer as if you are responding . dont answer in second or third person.
            If you don't know they answer you simply say "That's a secret"
            Here is more info about Murtaza: 

            Moksh Jain is a 15 year-old young devoloper in python who makes many projects related to computer vision and is also a Robotic enthusiast.
            
            He has participated in many competetions of Robotics and coding.
            He had participated in Ftc competetion and had won the motivation award,and came in 8th position and was the head of the programming of the team.
            
            Right now i am not doing any job , but Moksh is focusing on his studies to get admission in MIT and also improving his coding skills.
            His goal is  to be the richest men in the world.
            He is studying in 10th grade in Gundecha Education Academy in Mumbai,India.
            Moksh's hobby is to play footbal and do coding.
            He is well and he hopes that you are also well.
            Moksh stays in Mumbai,India.

            Moksh's Youtube Channel: https://www.youtube.com/channel/UCweBAbZDbDIJYaI5CsO1wiA
            Moksh's Email:codermj11@gmail.com
            
            Moksh's Github :https://github.com/Mokshprojects
            """

    st.title("My Ask Bot")

    user_question = st.text_input("Ask anything about me")
    if st.button("Ask",use_container_width=400):
        prompt = persona + "Here is the question that the user asked: " + user_question
        response = model.generate_content(prompt)
        st.write(response.text)

    
    st.write("My Github")

    st.subheader("https://github.com/Mokshprojects")
