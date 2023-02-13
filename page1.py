import streamlit as st

def page1():
    """Create the content for page 1 of the website."""
    import streamlit as st
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.linear_model import LinearRegression

    # Generate example sales data
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    sales = np.random.randint(0, 100, len(dates))
    df = pd.DataFrame({'date': dates, 'sales': sales})

    # Train linear regression model
    X = np.array(df['date'].astype(np.int64)/10**18).reshape(-1, 1)
    y = df['sales']
    reg = LinearRegression().fit(X, y)

    # Predict sales for future dates
    future_dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    future_X = np.array(future_dates.astype(np.int64)/10**18).reshape(-1, 1)
    future_sales = reg.predict(future_X)

    # Plot the results
    st.title("Project 1: Predicting Sales Trends")
    st.line_chart(df.set_index('date'))
    st.line_chart(pd.DataFrame({'date': future_dates, 'sales': future_sales}).set_index('date'))




