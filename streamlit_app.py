import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
from MainPage import *  
from page1 import *
from page2 import *
from page3 import *


page = st.sidebar.selectbox("Select a page", ["Main Page", "Project 1: Predicting Sales Trends", "Project 2: Exploring Customer Segmentation", "Project 3: Improving Supply Chain Efficiency"])
if page == "Main Page":
    main_content()
elif page == "Project 1: Predicting Sales Trends":
    page1()
elif page == "Project 2: Exploring Customer Segmentation":
    page2()
elif page == "Project 3: Improving Supply Chain Efficiency":
    page3()

