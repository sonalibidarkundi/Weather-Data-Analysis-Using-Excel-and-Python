# Pie Plot
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather_dataset_2025.csv")

# Average temperature by city
city_avg = df.groupby('City')['Temperature_C'].mean()

print(city_avg)

# pie Plot
city_avg.plot(kind='pie', autopct='%1.1f%%')
plt.title("Temperature Distribution by City")
plt.ylabel("")   # removes extra label
plt.show()