def page2():    
    from faker import Faker
    import pandas as pd
    import altair as alt
    fake = Faker()

    # Number of customers
    n_customers = 1000

    # Arrays to hold the generated data
    age = []
    salary = []
    gender = []
    cust_type = []
    spending_score = []

    # Generate the data
    for i in range(n_customers):
        age.append(fake.random_int(min=18, max=65, step=1))
        salary.append(fake.random_int(min=30, max=150, step=1) * 1000)
        gender.append(fake.random_element(elements=('Male', 'Female')))
        cust_type.append(fake.random_element(elements=('Casual', 'Loyal')))
        spending_score.append(fake.random_int(min=0, max=100, step=1))

    # Create a DataFrame from the generated data
    data = {'age': age, 'salary': salary, 'gender': gender, 'cust_type': cust_type, 'spending_score': spending_score}
    df = pd.DataFrame(data)

    # Save the DataFrame to a CSV file
    df.to_csv('customer_data.csv', index=False)

    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns


    st.title("Exploring Customer Segmentation")

    # Load the customer data from the CSV file
    df = pd.read_csv('customer_data.csv')

    st.subheader("Data Summary")
    st.write(df.head())
    st.write(df.describe())

    st.subheader("Data Distribution")

    # Plot a histogram of the age data
    st.write("Age Distribution of Customers")
    hist = alt.Chart(df).mark_bar().encode(
        alt.X("age", bin=alt.Bin(maxbins=30)),
        y='count()'
    )
    st.altair_chart(hist)

    # Plot a histogram of the salary data
    st.write("Salary Distribution of Customers")
    hist = alt.Chart(df).mark_bar().encode(
        alt.X("salary", bin=alt.Bin(maxbins=30)),
        y='count()'
    )
    st.altair_chart(hist)

    # Plot a bar chart of the gender data
    st.write("Gender Distribution of Customers")
    chart = alt.Chart(df).mark_bar().encode(
        x='gender',
        y='count()'
    )
    st.altair_chart(chart)

    # Plot a bar chart of the customer type data
    st.write("Customer Type Distribution of Customers")
    chart = alt.Chart(df).mark_bar().encode(
        x='cust_type',
        y='count()'
    )
    st.altair_chart(chart)

    # Plot a histogram of the spending score data
    st.write("Spending Score Distribution of Customers")
    hist = alt.Chart(df).mark_bar().encode(
        alt.X("spending_score", bin=alt.Bin(maxbins=30)),
        y='count()'
    )
    st.altair_chart(hist)

    st.subheader("Feature Relationships")

    # Plot a scatter plot of age vs. salary
    st.write("Age vs. Salary")
    chart = alt.Chart(df).mark_circle().encode(
        x='age',
        y='salary',
        color='gender',
        size='spending_score'
    )
    st.altair_chart(chart)

    # Plot a scatter plot of age vs. spending score
    st.write("Age vs. Spending Score")
    chart = alt.Chart(df).mark_circle().encode(
        x='age',
        y='spending_score',
        color='gender',
        size='salary'
    )
    st.altair_chart(chart)



