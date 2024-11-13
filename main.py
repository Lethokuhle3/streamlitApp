# main.py
import streamlit as st
from app import app_page
from contact import contact_page
from aboutUs import home_page

# Define a dictionary to map page names to their functions
PAGES = {
    "Home": home_page,
    "App": app_page,
    "Contact": contact_page,
}

# Create the sidebar menu
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Display the selected page with the navigation
page = PAGES[selection]
page()  # Call the function associated with the selected page
