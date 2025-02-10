import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r"C:\Users\user\car_price_dataset.csv"
df = pd.read_csv(file_path)

# Create a figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 12))  # 2 rows, 2 columns of subplots

# Line Chart: Trends in average price over years
if "Year" in df.columns and "Price" in df.columns:
    avg_price_per_year = df.groupby("Year")["Price"].mean()
    axes[0, 0].plot(avg_price_per_year.index, avg_price_per_year.values, marker='o', color='b')
    axes[0, 0].set_title("Average Car Price Over Years")
    axes[0, 0].set_xlabel("Year")
    axes[0, 0].set_ylabel("Average Price")
    axes[0, 0].grid()

# Bar Chart: Average price for each fuel type
if "Fuel_Type" in df.columns and "Price" in df.columns:
    avg_price_per_fuel = df.groupby("Fuel_Type")["Price"].mean()
    avg_price_per_fuel.plot(kind='bar', color='orange', ax=axes[0, 1])
    axes[0, 1].set_title("Average Price by Fuel Type")
    axes[0, 1].set_xlabel("Fuel Type")
    axes[0, 1].set_ylabel("Average Price")

# Histogram: Distribution of car prices
if "Price" in df.columns:
    sns.histplot(df["Price"], bins=30, kde=True, color='green', ax=axes[1, 0])
    axes[1, 0].set_title("Distribution of Car Prices")
    axes[1, 0].set_xlabel("Price")
    axes[1, 0].set_ylabel("Frequency")

# Scatter Plot: Relationship between Mileage and Price
if "Mileage" in df.columns and "Price" in df.columns:
    sns.scatterplot(x=df["Mileage"], y=df["Price"], alpha=0.7, color='purple', ax=axes[1, 1])
    axes[1, 1].set_title("Mileage vs Price")
    axes[1, 1].set_xlabel("Mileage")
    axes[1, 1].set_ylabel("Price")

# Adjust layout and display all plots
plt.tight_layout()
plt.show()



# Brief Documentation:

# 1. Line Chart: 
#    - Displays trends in average car prices over the years.
#    - X-axis represents the "Year," and Y-axis represents the "Average Price."
#    - Uses a grouped mean calculation for prices by year.

# 2. Bar Chart: 
#    - Compares average car prices based on the fuel type (e.g., Diesel, Electric).
#    - X-axis represents "Fuel Type," and Y-axis represents the "Average Price."
#    - Groups the data by 'Fuel_Type' and calculates the mean price for each type.

# 3. Histogram: 
#    - Visualizes the distribution of car prices in the dataset.
#    - X-axis represents "Price," and Y-axis represents the "Frequency" of prices.
#    - Includes a kernel density estimate (KDE) curve to indicate price distribution trends.

# 4. Scatter Plot:
#    - Examines the relationship between "Mileage" and "Price."
#    - X-axis represents "Mileage," and Y-axis represents "Price."
#    - Uses transparency (alpha) to handle overlapping data points.

# 5. Layout Adjustments:
#    - All four visualizations are displayed in a 2x2 grid within a single figure.
#    - The layout is adjusted for better spacing using `plt.tight_layout()`.

# 6. Output:
#    - Displays the combined figure containing all the visualizations in one window.

