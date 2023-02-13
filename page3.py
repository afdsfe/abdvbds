def page3():    

    from faker import Faker
    import pandas as pd
    import matplotlib.pyplot as plt
    import pandas as pd
    import streamlit as st
    import matplotlib.pyplot as plt
    import seaborn as sns
    # Initialize the Faker library
    fake = Faker()

    # Define the number of records to generate
    num_records = 1000

    # Create a list to store the supply chain data
    data = []

    # Generate fake data for the supply chain
    for i in range(num_records):
        # Generate fake data for a product
        product = fake.word()
        lead_time = fake.random_number(digits=3)
        inventory_level = fake.random_number(digits=3)
        transportation_cost = fake.random_number(digits=3)

        # Append the product data to the list
        data.append([product, lead_time, inventory_level, transportation_cost])

    # Convert the list to a Pandas dataframe
    df = pd.DataFrame(data, columns=["Product", "Lead Time", "Inventory Level", "Transportation Cost"])

    # Save the data to a CSV file
    df.to_csv("supply_chain_data.csv", index=False)

    # Load the supply chain dataset
    df = pd.read_csv("supply_chain_data.csv")

    lead_time_mean = df.groupby("Product")["Lead Time"].mean()

    # Plot the distribution of lead time for each product
    plt.figure(figsize=(10,5))
    sns.barplot(x=lead_time_mean.index, y=lead_time_mean.values)
    plt.xlabel("Product")
    plt.ylabel("Lead Time (Days)")
    st.pyplot()

    # Identify the products with the longest lead time
    longest_lead_time = lead_time_mean.nlargest(5)
    st.write("Products with longest lead time:", longest_lead_time)

    # Analyze Inventory Levels
    # Calculate the average inventory levels for each product
    inventory_mean = df.groupby("Product")["Inventory Level"].mean()

    # Plot the distribution of inventory levels for each product
    plt.figure(figsize=(10,5))
    sns.barplot(x=inventory_mean.index, y=inventory_mean.values)
    plt.xlabel("Product")
    plt.ylabel("Inventory Level (Units)")
    st.pyplot()

    # Identify the products with the lowest inventory levels
    lowest_inventory = inventory_mean.nsmallest(5)
    st.write("Products with lowest inventory levels:", lowest_inventory)

    # Analyze Transportation Costs
    # Calculate the average transportation costs for each product
    transportation_mean = df.groupby("Product")["Transportation Cost"].mean()

    # Plot the distribution of transportation costs for each product
    plt.figure(figsize=(10,5))
    sns.barplot(x=transportation_mean.index, y=transportation_mean.values)
    plt.xlabel("Product")
    plt.ylabel("Transportation Cost (USD)")
    st.pyplot()

    # Identify the products with the highest transportation costs
    highest_transportation = transportation_mean.nlargest(5)
    st.write("Products with highest transportation costs:", highest_transportation)

    # Conclusion and Recommendations
    st.write("Based on the analysis, you can identify the products with the longest lead time, lowest inventory levels, and highest transportation costs as the areas for improvement.")
    st.write("You can then make recommendations to reduce the lead time, increase inventory levels, and minimize transportation costs for these products to improve the efficiency of the supply chain.")