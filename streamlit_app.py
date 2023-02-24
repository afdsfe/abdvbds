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



# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import streamlit as st

# # Generate synthetic data for market risk
# np.random.seed(42)
# n_samples = 1000
# n_features = 10
# returns = pd.DataFrame(np.random.normal(0, 0.01, (n_samples, n_features)), columns=[f"Feature {i+1}" for i in range(n_features)])
# market = pd.DataFrame(np.random.normal(0, 0.005, n_samples), columns=["Market Return"])
# market_cap = pd.DataFrame(np.random.normal(0, 0.02, n_samples), columns=["Market Cap"])
# market_data = pd.concat([returns, market, market_cap], axis=1)

# # EDA
# st.title("Capital Market Risk Dataset - EDA")

# st.write("Market data sample:")
# st.write(market_data.head())

# st.write("Market data summary statistics:")
# st.write(market_data.describe())

# st.write("Market returns histogram:")
# fig, ax = plt.subplots()
# sns.histplot(data=market_data, x="Market Return", ax=ax)
# st.pyplot(fig)

# st.write("Market cap histogram:")
# fig, ax = plt.subplots()
# sns.histplot(data=market_data, x="Market Cap", ax=ax)
# st.pyplot(fig)

# # Risk analysis
# st.title("Capital Market Risk Dataset - Risk Analysis")

# st.write("Market returns vs. market cap scatter plot:")
# fig, ax = plt.subplots()
# sns.scatterplot(data=market_data, x="Market Return", y="Market Cap", ax=ax)
# st.pyplot(fig)

# st.write("Market returns vs. each feature scatter plot:")
# for i in range(n_features):
    # fig, ax = plt.subplots()
    # sns.scatterplot(data=market_data, x="Market Return", y=f"Feature {i+1}", ax=ax)
    # st.pyplot(fig)

