import streamlit as st

class MultiPage:
    def __init__(self):
        self.pages = []

    def add_page(self, title, func):
        self.pages.append({
            "title": title,
            "function": func
        })

    def run(self):
        # Apply custom CSS for selectbox and sidebar
        st.markdown("""
            <style>
                 /* Custom sidebar styles */
                /* This targets the entire sidebar background */
                div[role="complementary"] {
                    background-color: #000000;  /* Dark background for sidebar */
                    color: white;  /* White text in sidebar */
                }
                    
                /* Style the selectbox to remove rounded corners */
                .stSelectbox select {
                    background-color:#576d81;  /* Light background */
                    color: #333;  /* Dark text */
                    border: 2px solid #444;  /* Dark border */
                    border-radius: 0px;  /* Remove rounded corners */
                    padding: 10px;
                    font-size: 16px;
                }

                /* Style the selectbox options to have no circles and be flat */
                .stSelectbox option {
                    background-color: #5b5b5b;  /* Same as selectbox background */
                    color: #333;  /* Dark text */
                }

                /* Remove the circles and style the text on hover */
                .stSelectbox select:hover, .stSelectbox option:hover {
                    background-color: #5b5b5b;  /* Slightly darker background when hovered */
                }

                /* Title and text styling */
                .css-1v0mbd6 {
                    font-size: 18px;
                    font-weight: bold;
                    color: white;
                }

            </style>
        """, unsafe_allow_html=True)

        # Display the sidebar with a dropdown menu to select pages
        page = st.sidebar.selectbox(
            'Navigation',
            self.pages,
            format_func=lambda page: page['title']
        )
        
        # Run the selected page function
        page['function']()
