import pandas as pd

# Load the dataset
data = pd.read_csv("D:/Coding/Cognifyz_internship/Dataset.csv")

# Calculate the percentage of restaurants that offer online delivery
total_restaurants = len(data)

restaurants_with_delivery = len(data[data['Has Online delivery'] =="Yes"])
percentage_with_delivery = (restaurants_with_delivery / total_restaurants) * 100

print("Percentage of restaurants offering online delivery: ",format(percentage_with_delivery,".2f"),"%")

# Compare the average ratings of restaurants with and without online delivery
avg_rating_with_delivery = data[data['Has Online delivery'] == "Yes"]['Aggregate rating'].mean()
avg_rating_without_delivery = data[data['Has Online delivery'] == "No"]['Aggregate rating'].mean()

print("Average rating for restaurants with online delivery: ,",format(avg_rating_with_delivery,".2f"))
print("Average rating for restaurants without online delivery: ",format(avg_rating_without_delivery,".2f"))
