
import pandas as pd
import folium

# Load the dataset
data = pd.read_csv("D:/Coding/Cognifyz_internship/Dataset.csv")

# Create a map centered around a specific location
map_center = [data['Latitude'].mean(), data['Longitude'].mean()] 
restaurant_map = folium.Map(location=map_center, zoom_start=12)

# Add markers for each restaurant's location
for index, row in data.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Restaurant Name']).add_to(restaurant_map)

# Display the map
restaurant_map.save('restaurant_map.html')