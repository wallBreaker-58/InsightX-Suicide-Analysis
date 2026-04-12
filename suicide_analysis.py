# Import libraries
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("data.csv")

# Display first rows
df.head()

# Check missing values
#handling missing value
df.isnull().sum()

# Fill missing values with mean (for numerical columns)
df.fillna(df.mean(numeric_only=True), inplace=True)

# For categorical columns (if any missing)
df.fillna("Unknown", inplace=True)

# Check duplicates
#remove duplicates
df.duplicated().sum()

# Drop duplicates
df.drop_duplicates(inplace=True)

# Check datatypes
df.dtypes

# Example: Convert Year to int (if needed)
df['Year'] = df['Year'].astype(int)

# EDA data analysis
# Dataset info
df.info()
# Missing values
df.isnull().sum()
# Summary statistics
df.describe()
# Unique countries
df['CountryName'].nunique()
# Unique years
df['Year'].unique()
