import streamlit as st

def main_content():
    """Create the main content area of the website."""

    st.write("Data Analysis Projects")
    st.markdown(
        """
        ### Welcome to the Data Analysis Projects section!


        * **Predictive modeling:** Build models to make predictions based on historical data.
        * **Data visualization:** Use tools like `matplotlib`, `seaborn`, and `plotly` to create visually appealing and informative plots and charts.
        * **Exploratory data analysis (EDA):** Explore and understand data to identify trends, patterns, and relationships.
        * **Data cleaning and preprocessing:** Prepare data for analysis by handling missing values, outliers, and other inconsistencies.
        

        Here, I showcase some of the data analysis projects I have worked on.

        ### Project 1: Predicting Sales Trends

        In this project, I built a predictive model using historical sales data to forecast future sales trends. I used machine learning algorithms such as linear regression and decision trees to make accurate predictions. I also visualized the results using `matplotlib` and `seaborn` to give a clear understanding of the sales trends over time.

        ### Project 2: Exploring Customer Segmentation

        In this project, I performed exploratory data analysis (EDA) on customer data to identify different segments of customers based on their demographics and purchasing behavior. I used `pandas` and `numpy` to manipulate and analyze the data and `seaborn` to visualize the results. The insights gained from this project were used to inform targeted marketing efforts.

        ### Project 3: Improving Supply Chain Efficiency

        In this project, I used data from a logistics company to analyze and optimize their supply chain processes. I cleaned and preprocessed the data, and then used time-series analysis and simulation to identify bottlenecks and inefficiencies in the supply chain. I presented the results and recommended solutions to the company to improve their overall efficiency.
        """
    )