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

# Selecting important columns
df_selected = df[['Year', 'CountryName', 'Sex', 'AgeGroup',
                  'SuicideCount', 'DeathRatePer100K',
                  'GDPPerCapita', 'Population']]

# Total suicides per year
yearly_suicides = df.groupby('Year')['SuicideCount'].sum()

# Average suicide rate per year
avg_rate = df.groupby('Year')['DeathRatePer100K'].mean()

# Highest suicide year
yearly_suicides.idxmax()

# Lowest suicide year
yearly_suicides.idxmin()

import matplotlib.pyplot as plt

# Data visualization
# Line plot 
plt.figure()
yearly_suicides.plot()
plt.title("Suicide Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Total Suicides")
plt.show()

# Top countries analysis
top_countries = df.groupby('CountryName')['SuicideCount'].sum().sort_values(ascending=False).head(10)

plt.figure()
top_countries.plot(kind='bar')
plt.title("Top 10 Countries by Suicide Count")
plt.show()

# Gender distribution analysis
gender_data = df.groupby('Sex')['SuicideCount'].sum()

plt.figure()
gender_data.plot(kind='pie', autopct='%1.1f%%')
plt.title("Suicide Distribution by Gender")
plt.show()
