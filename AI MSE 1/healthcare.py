import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer  # Importing SimpleImputer

# Create a dummy dataset
data = {
    'age': [25, 30, 35, 40, 45, 50, np.nan, 60, 65, 70],
    'blood_pressure': [120, 130, 140, 150, np.nan, 160, 170, 180, 190, 200],
    'cholesterol': [200, 220, 240, 250, 260, 270, 280, 290, np.nan, 310],
    'symptom': ['Y', 'N', 'Y', 'Y', 'N', 'Y', 'Y', 'N', np.nan, 'Y'],
    'disease_outcome': [0, 1, 0, 1, 0, 1, 1, 0, 1, 0]  # 0 = No disease, 1 = Disease
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the dummy data to a CSV file
df.to_csv('healthcare_data.csv', index=False)

# Preview the dataset
print(df)

# Data Cleaning: Handling missing values (as shown in the previous code)
# Impute numerical columns with the median value
numerical_cols = df.select_dtypes(include=[np.number]).columns
imputer_num = SimpleImputer(strategy='median')  # Use SimpleImputer to handle missing data
df[numerical_cols] = imputer_num.fit_transform(df[numerical_cols])

# Impute categorical columns with the most frequent value (mode)
categorical_cols = df.select_dtypes(include=[object]).columns
imputer_cat = SimpleImputer(strategy='most_frequent')
df[categorical_cols] = imputer_cat.fit_transform(df[categorical_cols])

# Encoding Categorical Data
from sklearn.preprocessing import LabelEncoder  # Importing LabelEncoder for encoding categorical data

encoder = LabelEncoder()
for col in categorical_cols:
    df[col] = encoder.fit_transform(df[col])

# Now we can create figures to visualize the cleaned dataset.

# Set up the plotting environment
plt.figure(figsize=(10, 6))

# 1. Histogram of numerical columns
plt.subplot(2, 2, 1)  # 2 rows, 2 columns, 1st plot
df['age'].plot(kind='hist', bins=10, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')

# 2. Bar plot of disease_outcome distribution
plt.subplot(2, 2, 2)  # 2 rows, 2 columns, 2nd plot
df['disease_outcome'].value_counts().plot(kind='bar', color=['skyblue', 'lightgreen'], edgecolor='black')
plt.title('Disease Outcome Distribution')
plt.xlabel('Disease Outcome')
plt.ylabel('Count')

# 3. Box plot of blood_pressure and cholesterol
plt.subplot(2, 2, 3)  # 2 rows, 2 columns, 3rd plot
sns.boxplot(data=df[['blood_pressure', 'cholesterol']], palette='Set2')
plt.title('Blood Pressure & Cholesterol Distribution')
plt.ylabel('Value')

# Adjust layout for better spacing
plt.tight_layout()

# Show the first three plots
plt.show()

# Create a separate Pair Plot
sns.pairplot(df[['age', 'blood_pressure', 'cholesterol', 'disease_outcome']], hue='disease_outcome', palette='coolwarm')
plt.suptitle("Pair Plot: Features vs Disease Outcome", y=1.02)

# Show Pair Plot
plt.show()
