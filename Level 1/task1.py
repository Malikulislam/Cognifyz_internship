import pandas as pd

# Load the dataset
data = pd.read_csv("D:/Coding/Cognifyz_internship/Dataset.csv")

# Count the occurrences of each cuisine
cuisine_counts = data['Cuisines'].value_counts()

# Get the top three most common cuisines
top_three_cuisines = cuisine_counts.head(3)

# Calculate the total number of restaurants
total_restaurants = len(data)

# Calculate the percentage of restaurants for each top cuisine
percentage_of_restaurants = (top_three_cuisines / total_restaurants) * 100

# Display the top three cuisines and their percentages
print("Top Three Cuisines:")
for cuisine, percentage in percentage_of_restaurants.items():
    print(cuisine,":  restaurants (",format(percentage,".2f"),"%)")
