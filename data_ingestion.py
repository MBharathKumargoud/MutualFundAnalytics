import pandas as pd
import os

# File path
file_path = "data/raw/125497_nav.csv"

print("=" * 60)
print("DAY 1 - DATA INGESTION & QUALITY CHECK")
print("=" * 60)

# Check file exists
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    exit()

# Load dataset
df = pd.read_csv(file_path) 

# Dataset information
print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN DATA TYPES")
print(df.dtypes)

print("\nFIRST 5 ROWS")
print(df.head())

# Missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Duplicate rows
print("\nDUPLICATE RECORDS")
print(df.duplicated().sum())

# Convert date column if present
if "date" in df.columns:
    df["date"] = pd.to_datetime(
        df["date"],
        format="%d-%m-%Y",
        errors="coerce"
    )

# NAV statistics
if "nav" in df.columns:
    df["nav"] = pd.to_numeric(df["nav"], errors="coerce")

    print("\nNAV SUMMARY")
    print(df["nav"].describe())

# Date range
if "date" in df.columns:
    print("\nDATE RANGE")
    print("Start Date:", df["date"].min())
    print("End Date:", df["date"].max())

# Data quality summary
print("\n" + "=" * 60)
print("DATA QUALITY SUMMARY")
print("=" * 60)

total_rows = len(df)
total_columns = len(df.columns)
missing_values = df.isnull().sum().sum()
duplicate_rows = df.duplicated().sum()

print(f"Rows              : {total_rows}")
print(f"Columns           : {total_columns}")
print(f"Missing Values    : {missing_values}")
print(f"Duplicate Records : {duplicate_rows}")

# Save cleaned dataset
processed_path = "data/processed/nav_processed.csv"

os.makedirs("data/processed", exist_ok=True)

df.to_csv(processed_path, index=False)

print(f"\nProcessed file saved to:")
print(processed_path)

print("\nDay 1 Data Ingestion Completed Successfully!")