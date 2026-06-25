import pandas as pd
from sqlalchemy import create_engine
import os

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Folder containing cleaned CSVs
processed_folder = "data/processed"

# CSV file -> SQLite table mapping
datasets = {
    "nav_processed": "nav_processed.csv",
    "investor_transactions": "investor_transactions_clean.csv",
    "scheme_performance": "scheme_performance_clean.csv",
    "aum": "aum_clean.csv"
}

for table_name, csv_file in datasets.items():
    file_path = os.path.join(processed_folder, csv_file)

    if os.path.exists(file_path):
        df = pd.read_csv(file_path)

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"✅ {table_name}: {len(df)} rows loaded")
    else:
        print(f"❌ File not found: {csv_file}")

print("\n🎉 SQLite database created successfully!")
print("Database Name: bluestock_mf.db")