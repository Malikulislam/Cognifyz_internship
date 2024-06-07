import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("D:/Coding/Cognifyz_internship/Dataset.csv")

# Count the occurrences of each price range
price_range_counts = data['Price range']

# Calculate the total number of restaurants
total_restaurants = len(price_range_counts)

# Calculate the percentage of restaurants in each price range category
percentage_in_each_category = (price_range_counts.value_counts() / total_restaurants) * 100

# Create a bar chart
plt.figure(figsize=(8, 6))
plt.hist(price_range_counts, bins=[0,1,2,3,4], align='left', rwidth=0.8, color='orange')
plt.xlabel('Price Range')
plt.ylabel('Percentage of Restaurants')
plt.title('Distribution of Price Ranges Among Restaurants')
plt.xticks([0,1,2,3,4], ['Low', 'Mid', 'High', 'VeryHigh', 'Luxury'])  # Rotate x-axis labels if needed
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the percentage values on top of the bars
for index, value in enumerate(percentage_in_each_category):
    plt.text(index, value, f'{value:.2f}%', ha='center', va='bottom')
    print(f"Percentage of restaurent in Price Range {index}: {value:.2f}%")

# Show the bar chart
plt.tight_layout()
plt.show()