import pandas as pd

# Load the dataset
data = pd.read_csv("D:/Coding/Cognifyz_internship/Dataset.csv")

# Extract the "Cuisines" and "Aggregate rating" columns
cuisine_ratings = data[['Cuisines', 'Aggregate rating']].dropna()

# Identify common cuisine combinations
cuisine_ratings['Cuisines'] = cuisine_ratings['Cuisines'].str.split(", ")
cuisine_ratings['Cuisines'] = cuisine_ratings['Cuisines'].apply(lambda x: tuple(sorted(x)))  

# Count common combinations
common_combinations = cuisine_ratings['Cuisines'].value_counts().head(18)

# Analyze ratings for cuisine combinations
average_ratings = cuisine_ratings.groupby("Cuisines")['Aggregate rating'].mean()

# Display results
print("Most Common Cuisine Combinations:")
print(common_combinations)

print("Average Ratings for Cuisine Combinations:")
for combination, count in common_combinations.items():
    combination_str = ', '.join(combination)
    average_rating = average_ratings[combination]
    print("Cuisines: ",combination_str," | Count: ",count," | Average Rating: ",format(average_rating,".2f"))