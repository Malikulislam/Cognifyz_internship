import pandas as pd
#Load the  dataset
data =pd.read_csv("D:/Coding/Cognifyz_internship/Dataset.csv")

restaurent_per_city = data['City'].value_counts()

avg_rating_per_city= data.groupby('City')["Aggregate rating"].mean()

city_most_restaurents = restaurent_per_city.idxmax()
num_restarants_most = restaurent_per_city.max()

city_highest_avg_rating = avg_rating_per_city.idxmax()
highest_avg_rating = avg_rating_per_city.max()
#Display the city with highest number of restaurents
print("City with the Highest number of Restaurents:")
print(city_most_restaurents," with ",num_restarants_most," restaurent")
#Display the city with highest average rating
print("\nCity with Highest Average Rating:")
print(city_highest_avg_rating," with an average rating of ",format(highest_avg_rating,".2f"))