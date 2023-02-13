import streamlit as st
from PIL import Image
def header():
    """Create a header for the website."""
    image = Image.open("./bear.jpg")
    image = image.resize((100, 50))
    logo_image = st.image(image)
    st.header("Header")

def footer():
    """Create a footer for the website."""
    st.write("Footer")

def main_content():
    """Create the main content area of the website."""
    st.write("Main Content")

from page1 import page1

def page2():
    """Create the second page of the website."""
    st.write("Page 2")

def page3():
    """Create the third page of the website."""
    st.write("Page 3")

def run_app():
    """Run the Streamlit app."""
    header()
    page = st.sidebar.selectbox("Select a page", ["Main Content", "Page 1", "Page 2", "Page 3"])
    if page == "Main Content":
        main_content()
    elif page == "Page 1":
        page1()
    elif page == "Page 2":
        page2()
    elif page == "Page 3":
        page3()
    footer()

if __name__ == "__main__":
    run_app()
