import streamlit as st
import re
import requests



def app():


    WEBHOOK_URL = st.secrets["WEBHOOK_URL"]


    def is_valid_email(email):
        # Basic regex pattern for email validation
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_pattern, email) is not None

    col1,col2 = st.columns(2)
    with col1:


        st.subheader("<Yo✌️>")
        st.title("My Name Is Moksh Jain,A young devoloper")
    with col2:
        st.image("images/MokshPort.png",width=300)

        def contact_form():
            with st.form("contact_form"):
                name = st.text_input("First Name")
                email = st.text_input("Email Address")
                message = st.text_area("Your Message")
                submit_button = st.form_submit_button("Submit")

            if submit_button:
                if not WEBHOOK_URL:
                    st.error("Email service is not set up. Please try again later.", icon="📧")
                    st.stop()

                if not name:
                    st.error("Please provide your name.", icon="🧑")
                    st.stop()

                if not email:
                    st.error("Please provide your email address.", icon="📨")
                    st.stop()

                if not is_valid_email(email):
                    st.error("Please provide a valid email address.", icon="📧")
                    st.stop()

                if not message:
                    st.error("Please provide a message.", icon="💬")
                    st.stop()

                # Prepare the data payload and send it to the specified webhook URL
                data = {"email": email, "name": name, "message": message}
                response = requests.post(WEBHOOK_URL, json=data)

                if response.status_code == 200:
                    st.success("Your message has been sent successfully! 🎉", icon="🚀")
                else:
                    st.error("There was an error sending your message.", icon="😨")



        @st.experimental_dialog("Contact Me")
        def show_contact_form():
            contact_form()

        if st.button("✉️ Contact Me"):
            show_contact_form()

    st.title("")
    st.write("My name is Moksh Jain .I am a robotics enthusiast and a passionate coder, as well as a young developer currently studying in 10th grade in India. I have created several apps and participated in many competitions, always striving to push the boundaries of my knowledge and skills. My ultimate goal is to become the best programmer in the world, and I am dedicated to achieving this through continuous learning and innovation.")




