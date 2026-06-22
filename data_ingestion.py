import pandas as pd

# Load data
df = pd.read_csv("data/raw/125497_nav.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")

# Sort oldest to newest
df = df.sort_values("date")

# Daily return %
df["daily_return"] = df["nav"].pct_change() * 100

# Save processed data
df.to_csv("data/processed/nav_processed.csv", index=False)

print(df.head())
print("\nProcessed data saved successfully!")

# CAGR
start_nav = df["nav"].iloc[0]
end_nav = df["nav"].iloc[-1]

years = (df["date"].iloc[-1] - df["date"].iloc[0]).days / 365.25

cagr = ((end_nav / start_nav) ** (1 / years) - 1) * 100

# Volatility
volatility = df["daily_return"].std() * (252 ** 0.5)

# Drawdown
df["cum_max"] = df["nav"].cummax()
df["drawdown"] = (df["nav"] - df["cum_max"]) / df["cum_max"] * 100

max_drawdown = df["drawdown"].min()

print(f"\nCAGR: {cagr:.2f}%")
print(f"Annualized Volatility: {volatility:.2f}%")
print(f"Maximum Drawdown: {max_drawdown:.2f}%")