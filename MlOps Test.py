import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Create a random DataFrame
df = pd.DataFrame({
    'A': np.random.randn(100),
    'B': np.random.rand(100) * 100,
    'C': np.random.randint(0, 50, size=100),
    'D': np.random.choice([0, 1], size=100)
})

# Add a random 'Category' column for grouping
df['Category'] = np.random.choice(['X', 'Y', 'Z'], size=100)

# Compute basic statistics
print("Column Means:\n", df.mean(numeric_only=True))
print("\nColumn Sums:\n", df.sum(numeric_only=True))
print("\nColumn Standard Deviations:\n", df.std(numeric_only=True))

# Add a new column 'E' as a linear combination of A, B, and C
df['E'] = 0.5 * df['A'] + 0.3 * df['B'] - 0.2 * df['C']

# Filter rows where 'A' is above its mean
mean_A = df['A'].mean()
filtered_df = df[df['A'] > mean_A]

print(f"\nNumber of rows where 'A' > mean ({mean_A:.2f}):", len(filtered_df))

# Group by 'Category' and compute mean of numeric columns
grouped_stats = df.groupby('Category').mean(numeric_only=True)
print("\nGrouped Means by Category:\n", grouped_stats)

# Just a comment to change
df.to_csv("test.csv", index=False)


