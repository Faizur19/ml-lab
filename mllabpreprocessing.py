import pandas as pd

# Step 1: Create / Load Dataset
data = {
    "student_id": [1, 2, 3, 4, 5, 5],
    "internal_marks": [20, 25, None, 30, 100, 100],
    "external_marks": [60, 65, 70, None, 200, 200],
    "attendance": [80, 85, 90, 95, 50, 50],
    "age": [18, 19, 20, 21, 100, 100],
    "result": [1, 1, 1, 1, 0, 0]
}

df = pd.DataFrame(data)

print("Original Data:\n", df)

# Step 2: Fill missing values with mean
df = df.fillna(df.mean(numeric_only=True))

print("\nAfter Filling Missing Values:\n", df)

# Step 3: Remove duplicate rows
df = df.drop_duplicates()

print("\nAfter Removing Duplicates:\n", df)

# Step 4: Min-Max Normalization
# Formula: (x - min) / (max - min)

df_norm = df.copy()

for col in ["internal_marks", "external_marks", "attendance", "age"]:
    df_norm[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

print("\nAfter Min-Max Normalization:\n", df_norm)

# Step 5: Detect and Remove Outliers using IQR

df_clean = df.copy()

for col in ["internal_marks", "external_marks", "attendance", "age"]:
    Q1 = df_clean[col].quantile(0.25)
    Q3 = df_clean[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df_clean = df_clean[(df_clean[col] >= lower) & (df_clean[col] <= upper)]

print("\nAfter Removing Outliers:\n", df_clean)