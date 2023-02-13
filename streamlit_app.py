import streamlit as st

def header():
    """Create a header for the website."""
    st.header("Header")

def footer():
    """Create a footer for the website."""
    st.footer("Footer")

def main_content():
    """Create the main content area of the website."""
    st.write("Main Content")

def run_app():
    """Run the Streamlit app."""
    header()
    main_content()
    footer()

if __name__ == "__main__":
    run_app()
