import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather_dataset_2025.csv")

# Average temperature by city
city_avg = df.groupby('City')['Temperature_C'].mean()

print(city_avg)

# Histogram Plot
city_avg.plot(kind='hist', bins=10)
plt.title("Average Temperature by City")
plt.xlabel("City")
plt.ylabel("Temperature")
plt.xticks(rotation=45)
plt.show()