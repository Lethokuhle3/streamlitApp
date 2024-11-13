# contact.py
import streamlit as st


def contact_page():
    st.title("Contact Page")
    st.write("Get in touch with us for any queries! ")
    # Additional contact page content can go here



    # Contact form
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")

    if st.button("Submit"):
        st.write("Thank you for reaching out! We will get back to you shortly.")
