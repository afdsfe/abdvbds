import pandas as pd
import random
import numpy as np

import streamlit as st
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False) 

# Function to generate random integer for credit score
def random_credit_score():
    return random.randint(300, 850)

# Function to generate random string for loan purpose
def random_loan_purpose():
    purposes = ['Home Improvement', 'Debt Consolidation', 'Business', 'Auto', 'Education', 'Other']
    return random.choice(purposes)

# Function to generate random integer for annual income
def random_annual_income():
    return random.randint(25000, 500000)

# Function to generate random string for employment status
def random_employment_status():
    statuses = ['Employed', 'Self-Employed', 'Unemployed', 'Retired']
    return random.choice(statuses)

# Function to generate random string for loan status
def random_loan_status():
    statuses = ['Approved', 'Denied', 'Cancelled', 'Pending']
    return random.choice(statuses)

# Function to generate random float for loan amount
def random_loan_amount():
    return random.uniform(1000.0, 100000.0)

# Function to generate random date for loan date
def random_loan_date():
    start = np.datetime64('2010-01-01')
    end = np.datetime64('2023-01-01')
    return np.datetime64(random.randint(start.astype(int), end.astype(int)), 'D').astype(object)

# Function to generate random float for interest rate
def random_interest_rate():
    return random.uniform(0.05, 0.35)

# Dataset - bank_risk
credit_scores = [random_credit_score() for i in range(1000)]
loan_purposes = [random_loan_purpose() for i in range(1000)]
annual_incomes = [random_annual_income() for i in range(1000)]
employment_statuses = [random_employment_status() for i in range(1000)]
loan_statuses = [random_loan_status() for i in range(1000)]
loan_amounts = [random_loan_amount() for i in range(1000)]
loan_dates = [random_loan_date() for i in range(1000)]
interest_rates = [random_interest_rate() for i in range(1000)]

bank_risk = {'Credit_Score': credit_scores,
             'Loan_Purpose': loan_purposes,
             'Annual_Income': annual_incomes,
             'Employment_Status': employment_statuses,
             'Loan_Status': loan_statuses,
             'Loan_Amount': loan_amounts,
             'Loan_Date': loan_dates,
             'Interest_Rate': interest_rates}

df_bank_risk = pd.DataFrame(bank_risk)

# Add a title to the sidebar
st.sidebar.title("Navigation")

# Create a menu selection to navigate between pages
menu = ["Page 1", "Page 2", "Page 3","Page 4"]
selected_page = st.sidebar.selectbox("Select a page", menu)

# Create separate functions for each page
def page_1():
    st.write("This is page 1")
    st.title("Bank Risk Dataset")
    st.write("A sample of 1000 loan applications with various attributes including credit score, loan purpose, annual income, employment status, loan status, loan amount, loan date, and interest rate.")

    st.dataframe(df_bank_risk)

    if st.checkbox("Show Scatter Plot of Interest_Rate and Credit_Score"):
        plt.scatter(df_bank_risk['Interest_Rate'], df_bank_risk['Credit_Score'])
        plt.xlabel("Interest_Rate")
        plt.ylabel("Credit_Score")
        st.pyplot()

def page_2():
    st.write("This is page 2")
    st.title("Bank Risk EDA")

    # Load the dataset
    
    
    # Show the first 5 rows of the dataset
    st.write("First 5 rows of the dataset:")
    st.write(df_bank_risk.head())
    
    # Show the descriptive statistics for the numerical variables
    st.write("Descriptive statistics for numerical variables:")
    st.write(df_bank_risk.describe())
    
    # Plot the distribution of the credit scores
    st.write("Distribution of credit scores:")
    sns.distplot(df_bank_risk['Credit_Score'])
    st.pyplot()
    
    # Plot the distribution of the loan amounts
    st.write("Distribution of loan amounts:")
    sns.distplot(df_bank_risk['Loan_Amount'])
    st.pyplot()
    
    # Show the countplot for the loan purpose variable
    st.write("Countplot for loan purpose:")
    sns.countplot(x='Loan_Purpose', data=df_bank_risk)
    st.pyplot()
    
    # Show the countplot for the employment status variable
    st.write("Countplot for employment status:")
    sns.countplot(x='Employment_Status', data=df_bank_risk)
    st.pyplot()
    
    # Show the countplot for the loan status variable
    st.write("Countplot for loan status:")
    sns.countplot(x='Loan_Status', data=df_bank_risk)
    st.pyplot()
    
    # Calculate the correlation matrix
    corr = df_bank_risk.corr()
    
    # Create a heatmap using Seaborn
    st.write("Correlation heatmap:")
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    st.pyplot()
    
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import streamlit as st
import time
import networkx as nx
def page_3():
    st.write("This is page 3")

    
    st.title("Data Flow Diagram")
    
    G = nx.DiGraph()
    
    G.add_node("Data Source")
    G.add_node("Data Cleaning")
    G.add_node("Data Transformation")
    G.add_node("Data Analysis")
    G.add_node("Data Visualization")
    
    G.add_edge("Data Source", "Data Cleaning")
    G.add_edge("Data Cleaning", "Data Transformation")
    G.add_edge("Data Transformation", "Data Analysis")
    G.add_edge("Data Analysis", "Data Visualization")
    
    pos = nx.spring_layout(G)
    
    nx.draw(G, pos, with_labels=True)
    
    st.pyplot()
import pandas as pd
import random
import datetime
import csv
import random
import datetime
def page_4():
    st.write("This is page 3")
    import sqlite3
    # from faker import Faker
    # fake = Faker()

    # Connect to a SQLite database
    conn = sqlite3.connect("./AdventureWorks.db")
    cursor = conn.cursor()

    # # Create the customers table
    # cursor.execute("""
    # CREATE TABLE IF NOT EXISTS customers (
        # customer_id INTEGER PRIMARY KEY,
        # customer_name TEXT,
        # customer_address TEXT,
        # customer_email TEXT,
        # customer_phone_number TEXT
    # )
    # """)

    # # Create the products table
    # cursor.execute("""
    # CREATE TABLE IF NOT EXISTS products (
        # product_id INTEGER PRIMARY KEY,
        # product_name TEXT,
        # product_description TEXT,
        # product_price REAL
    # )
    # """)

    # # Create the orders table
    # cursor.execute("""
    # CREATE TABLE IF NOT EXISTS orders (
        # order_id INTEGER PRIMARY KEY,
        # order_date TEXT,
        # customer_id INTEGER,
        # product_id INTEGER,
        # order_quantity INTEGER,
        # FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
        # FOREIGN KEY (product_id) REFERENCES products(product_id)
    # )
    # """)

    # # Define the number of fake records to generate
    # customers_records = 100000
    # products_records = 100000
    # orders_records = 100000

    # # Generate fake customers data and insert into the database
    # for i in range(customers_records):
        # customer_id = i + 1
        # customer_name = fake.name()
        # customer_address = fake.address()
        # customer_email = fake.email()
        # customer_phone_number = fake.phone_number()
        
        # cursor.execute("""
        # INSERT INTO customers (customer_id, customer_name, customer_address, customer_email, customer_phone_number)
        # VALUES (?, ?, ?, ?, ?)
        # """, (customer_id, customer_name, customer_address, customer_email, customer_phone_number))

    # # Generate fake products data and insert into the database
    # for i in range(products_records):
        # product_id = i + 1
        # product_name = fake.word()
        # product_description = fake.sentence()
        # product_price = fake.random_int(min=10, max=1000, step=1)
        
        # cursor.execute("""
        # INSERT INTO products (product_id, product_name, product_description, product_price)
        # VALUES (?, ?, ?, ?)
        # """, (product_id, product_name, product_description, product_price))

    # # Generate fake orders data and insert into the database
    # for i in range(orders_records):
        # order_id = i + 1
        # order_date = fake.date_this_decade()
        # customer_id = fake.random_int(min=1, max=customers_records, step=1)
        # product_id = fake.random_int(min=1, max=products_records, step=1)
        # order_quantity = fake.random_int(min=1, max=100, step=1)
        # cursor.execute("""
    # INSERT INTO orders (order_id, order_date, customer_id, product_id, order_quantity)
    # VALUES (?, ?, ?, ?, ?)
    # """, (order_id, order_date, customer_id, product_id, order_quantity))
    st.dataframe(pd.read_sql('select * from orders',con=conn))
    conn.commit()
    conn.close()   

# Use a dictionary to map the menu selection to the corresponding page function
pages = {"Page 1": page_1,
         "Page 2": page_2,
         "Page 3": page_3,
         "Page 4": page_4
         }

# Call the selected page function
pages[selected_page]()
    


    
    
# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# if st.checkbox("Show Corr of Interest_Rate and Credit_Score"):
	# st.title("Bank Risk Heatmap")

	# # Load the dataset
	# #df_bank_risk = pd.read_csv('bank_risk.csv')

	# # Calculate the correlation matrix
	# corr = df_bank_risk.corr()

	# # Create a heatmap using Seaborn
	# sns.heatmap(corr, annot=True, cmap='coolwarm')

	# # Show the plot
	# st.pyplot()  




