import pandas as pd

# Load the dataset
file_path = r"C:\Users\user\car_price_dataset.csv"
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("Initial dataset preview:")
print(data.head())

# Check the dataset structure
print("\nDataset info:")
data.info()

# Display the data types of all columns
print("\nData types of all columns:")
print(data.dtypes)

# Identify rows with missing values
rows_with_missing = data[data.isnull().any(axis=1)]

# Display rows with missing values
print("\nRows with missing values:")
print(rows_with_missing)

# Display the number of missing values per column
print("\nNumber of missing values per column:")
print(data.isnull().sum())

# Calculate the mean of relevant numerical columns
numerical_columns = ['Mileage', 'Price']
mean_values = data[numerical_columns].mean()
print("\nMean values for relevant columns:")
print(mean_values)

# Verify the first few rows of the updated dataset
print("\nPreview of the updated dataset:")
print(data.head())

# Optionally, save the cleaned dataset to a new CSV file
cleaned_file_path = r"C:\Users\user\car_price_dataset_cleaned.csv"
data.to_csv(cleaned_file_path, index=False)
print(f"\nCleaned dataset saved to {cleaned_file_path}")

# Drop rows with any missing values
cleaned_data = data.dropna()

# Display the number of rows and columns after dropping missing values
print(f"Dataset shape after dropping rows with missing values: {cleaned_data.shape}")

# Save the cleaned dataset to a new CSV file
cleaned_file_path = r"C:\Users\user\car_price_dataset_cleaner.csv"
cleaned_data.to_csv(cleaned_file_path, index=False)
print(f"Cleaned dataset saved to {cleaned_file_path}")

# Optional: Display the first few rows of the cleaned dataset
print("\nPreview of the cleaned dataset:")
print(cleaned_data.head())


# Summary of steps performed:
# 1. Loaded the dataset from a CSV file.
# 2. Displayed initial data preview and structure information.
# 3. Identified and displayed rows with missing values.
# 4. Calculated and displayed mean values for 'Mileage' and 'Price' columns.
# 5. Saved the original dataset to a new CSV file.
# 6. Dropped rows containing any missing values.
# 7. Saved the cleaned dataset to a new CSV file.
# 8. Displayed a preview of the cleaned dataset.