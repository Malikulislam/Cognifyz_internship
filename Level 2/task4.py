import pandas as pd

# Load the dataset
data = pd.read_csv("D:/Coding/Cognifyz_internship/Dataset.csv")

# Group data by Restaurant Name to identify chains
chain_groups = data.groupby('Restaurant Name')

# Initialize lists to store chain statistics
chain_names = []
chain_avg_ratings = []
chain_total_votes = []
chain_num_locations = []

# Calculate chain statistics
for chain_name, group in chain_groups:
    num_locations = len(group)
    avg_rating = group['Aggregate rating'].mean()
    total_votes = group['Votes'].sum()

    chain_names.append(chain_name)
    chain_avg_ratings.append(avg_rating)
    chain_total_votes.append(total_votes)
    chain_num_locations.append(num_locations)

# Create a DataFrame for chain statistics
chain_stats = pd.DataFrame({
    'Chain Name': chain_names,
    'Average Rating': chain_avg_ratings,
    'Total Votes': chain_total_votes,
    'Number of Locations': chain_num_locations
})

# Display chain statistics sorted by Number of Locations in descending order
chain_stats = chain_stats.sort_values(by="Number of Locations", ascending=False)
print("Chain Statistics:")
print(chain_stats)
