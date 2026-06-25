import pandas as pd
import glob
import os

os.makedirs("data/processed", exist_ok=True)

# -----------------------
# NAV FILES CLEANING
# -----------------------

nav_files = glob.glob("data/raw/*_nav.csv")

nav_dfs = []

for file in nav_files:
    df = pd.read_csv(file)

    amfi_code = os.path.basename(file).split("_")[0]
    df["amfi_code"] = amfi_code

    nav_dfs.append(df)

nav_df = pd.concat(nav_dfs, ignore_index=True)

print("NAV rows before cleaning:", len(nav_df))

# Remove duplicates
nav_df.drop_duplicates(inplace=True)

# Save merged NAV
nav_df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("NAV cleaned successfully")


# -----------------------
# INVESTOR TRANSACTIONS
# -----------------------

txn = pd.read_csv(
    "data/raw/investor_transactions.csv"
)

txn.drop_duplicates(inplace=True)

txn["amount"] = pd.to_numeric(
    txn["amount"],
    errors="coerce"
)

txn = txn[txn["amount"] > 0]

txn.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Transactions cleaned")


# -----------------------
# SCHEME PERFORMANCE
# -----------------------

perf = pd.read_csv(
    "data/raw/scheme_performance.csv"
)

perf.drop_duplicates(inplace=True)

perf.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("Performance cleaned")


# -----------------------
# AUM
# -----------------------

aum = pd.read_csv(
    "data/raw/aum.csv"
)

aum.drop_duplicates(inplace=True)

aum.to_csv(
    "data/processed/aum_clean.csv",
    index=False
)

print("AUM cleaned")

print("All files cleaned successfully")