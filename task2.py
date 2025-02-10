import pandas as pd

# Load the dataset
file_path = r"C:\Users\user\car_price_dataset.csv"
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("Dataset preview:")
print(df.head())

# Compute basic statistics for numerical columns
print("\nBasic statistics for numerical columns:")
print(df.describe())

# Perform groupings by 'Fuel_Type' and compute the mean 'Price'
if 'Fuel_Type' in df.columns and 'Price' in df.columns:
    grouped = df.groupby("Fuel_Type")["Price"].mean()
    print("\nMean price for each fuel type:")
    print(grouped)
else:
    print("\nColumns 'Fuel_Type' or 'Price' not found in the dataset.")

# Insights or interesting findings
if 'Fuel_Type' in df.columns and 'Price' in df.columns:
    highest_avg_price = grouped.idxmax()
    highest_avg_price_value = grouped.max()
    print("\nInteresting findings:")
    print(f"The fuel type with the highest average price is {highest_avg_price} "
          f"with an average price of {highest_avg_price_value}.")
else:
    print("\nCannot compute insights due to missing columns.")




# Brief Documentation

# 1. Dataset Loading:
#    - The dataset is loaded from the specified file path into a Pandas DataFrame using `pd.read_csv()`.

# 2. Dataset Preview:
#    - The first few rows of the dataset are displayed using `df.head()` to provide an initial overview.

# 3. Basic Statistics:
#    - Descriptive statistics for all numerical columns are calculated and displayed using `df.describe()`.

# 4. Grouping by 'Fuel_Type':
#    - The code groups the data by the 'Fuel_Type' column and computes the mean of the 'Price' column for each fuel type using `groupby()`.

# 5. Insights:
#    - Finds the fuel type with the highest average price and displays its name and the corresponding value.

# 6. Error Handling:
#    - Ensures that the required columns ('Fuel_Type' and 'Price') exist in the dataset before performing operations.
