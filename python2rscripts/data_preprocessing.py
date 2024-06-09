import pandas as pd

# Load the dataset
df = pd.read_csv('../data/dataset.csv')

# Preprocess the data
df['new_column'] = df['existing_column'] * 2

# Save the processed data
df.to_csv('../data/processed_dataset.csv', index=False)
