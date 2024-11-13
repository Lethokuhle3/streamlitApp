# app.py
import streamlit as st

st.set_page_config(page_title="Letho's House Marketplace", page_icon="🏠", layout="wide")

def app_page():
    st.title("Welcome to Letho's House Marketplace!")
    user_input = st.text_input("Enter something:")
    user_input =st.text_input("What is your name:")


    st.header("HOUSES ON SALE!!")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("assets\WhatsApp Image 2024-11-05 at 11.44.18.jpeg")
        st.write("A beatiful home in the Eastlands")

    with col2:
        
        st.image("assets\WhatsApp Image 2024-11-05 at 11.44.25 (1).jpeg" )
        st.write("A beautiful house in the pearls of Umhlanga ")

    with col3:
        st.image("assets\WhatsApp Image 2024-11-05 at 11.44.23.jpeg")
        st.write("Situated in the Netherelands")


    VIDEO_URL = "https://www.youtube.com/watch?v=plt2Gbxd3a0"
    st.video(VIDEO_URL)

app_page()



