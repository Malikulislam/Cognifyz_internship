import pandas as pd

# Load the dataset into a pandas DataFrame
data = pd.read_csv("D:/Coding/Cognifyz_internship/Dataset.csv")

# Extract the relevant columns
subset_data = data[['Price range', 'Has Online delivery', 'Has Table booking']]

# Create a cross-tabulation
cross_tab = pd.crosstab(subset_data['Price range'], [subset_data['Has Online delivery'], subset_data['Has Table booking']])

# Calculate percentages of online delivery and table booking by price range
percentage_table = cross_tab.div(cross_tab.sum(1), axis=0) * 100

# Display results
print("Cross-Tabulation: Price Range vs. Online Delivery and Table Booking")
print(cross_tab)
print("\nPercentages of Online Delivery and Table Booking by Price Range:")
print(percentage_table)
     