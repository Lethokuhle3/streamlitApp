# menu.py
import streamlit as st

def home_page():
    st.title("Our Story")
    st.image("assets\WhatsApp Image 2024-11-05 at 11.44.22 (2).jpeg", use_column_width=True, caption="Building Communities, One Home at a Time")
    st.write("Welcome to the home page of the application!")
  
    st.header("Our History")
    st.write("""
    Founded in 2000, our journey began with a mission to make property buying simple and accessible.
    Starting with a small team, we aimed to bridge the gap between buyers and sellers in the housing market.
    Over the years, we’ve grown into a trusted platform, connecting people with their dream homes and investment properties.
    """)

    st.subheader("Our Mission")
    st.write("""
    To simplify the home-buying experience by providing comprehensive, transparent, and trustworthy listings.
    We believe in empowering buyers with the right information to make confident decisions.
    """)

    st.subheader("Our Vision")
    st.write("""
    We envision a world where finding a home is as easy as a few clicks,
    where everyone has access to the tools and support needed to own or invest in property.
    """)

    # Core Values section
    st.subheader("Our Values")
    st.write("""
    - **Integrity:** We prioritize honesty and transparency in every listing and transaction.
    - **Innovation:** We constantly improve to provide the best experience for our users.
    - **Customer Focus:** We’re committed to understanding and fulfilling our users’ needs.
    - **Community:** We believe in building and supporting vibrant communities.
    """)

    # Call-to-action section
    st.markdown("### Ready to start your journey?")
    st.write("Explore our listings and discover your next home!")
    if st.button("Explore Listings"):
        # Link this to the main page or listings page in your app
        st.write("Redirecting to the Listings page...")

# Call the function
