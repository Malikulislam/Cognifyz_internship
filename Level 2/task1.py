import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("D:/Coding/Cognifyz_internship/Dataset.csv")

# Analyze the distribution of aggregate ratings
plt.figure(figsize=(8, 6))
plt.hist(data['Aggregate rating'], bins=10, color='orange', edgecolor='black')
plt.xlabel('Aggregate rating')
plt.ylabel('Frequency')
plt.title('Distribution of Aggregate Ratings')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Finding the most common rating range
rating_counts = data['Aggregate rating'].value_counts()
most_common_rating = rating_counts.idxmax()
most_common_rating_count = rating_counts.max()

print("Most common rating range: ",most_common_rating," (",most_common_rating_count," restaurants)")

# Calculating the average number of votes received by restaurants
average_votes = data['Votes'].mean()
print("Average number of votes received by restaurants: ",format(average_votes,".2f"))

# display 
plt.tight_layout()
plt.show()