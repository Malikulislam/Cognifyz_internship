import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a pandas DataFrame
data = pd.read_csv("D:/Coding/Cognifyz_internship/Dataset.csv")

# Identify restaurants with the highest and lowest votes
highest_votes_restaurant = data[data['Votes'] == data['Votes'].max()]
lowest_votes_restaurant = data[data['Votes'] == data['Votes'].min()]

# Analyze correlation between votes and rating
correlation = data['Votes'].corr(data['Aggregate rating'])

# Display results
print("Restaurant with Highest votes:")
print(highest_votes_restaurant[['Restaurant Name', 'Votes', 'Aggregate rating']])

print("\nRestaurant with Lowest votes:")
print(lowest_votes_restaurant[['Restaurant Name', 'Votes', 'Aggregate rating']])

print("\nCorrelation between Votes and Rating:", correlation)

# Scatter plot for correlation visualization
plt.scatter(data['Votes'], data['Aggregate rating'])
plt.xlabel('Votes')
plt.title('Votes vs. Aggregate Rating')
plt.ylabel('Aggregate Rating')
plt.show()
