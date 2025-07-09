import pandas as pd

# Load dataset with relevant columns
df = pd.read_csv('crime_dataset_india.csv', usecols=['Crime Description', 'Crime Domain'])

# Drop rows with missing values
df = df.dropna()

# Optional: sample 20,000 rows for fast training
df = df.sample(20000, random_state=42).reset_index(drop=True)

print(df['Crime Domain'].value_counts())

# Save smaller cleaned dataset
df.to_csv('india_crime_small.csv', index=False)
