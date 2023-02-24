import streamlit as st

def main():
    menu = ["Page 1", "Page 2", "Page 3"]
    page = "Page 1"

    st.sidebar.header("Navigation")
    for m in menu:
        if st.sidebar.button(m):
            page = m

    st.header("Content")
    if page == "Page 1":
        st.write("This is Page 1")
    elif page == "Page 2":
        st.write("This is Page 2")
    elif page == "Page 3":
        st.write("This is Page 3")

if __name__ == "__main__":
    main()
