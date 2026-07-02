
import pandas as pd

def recommend_funds(df, risk_level):

    if risk_level.lower()=="low":
        return df.sort_values("expense_ratio").head(3)

    elif risk_level.lower()=="moderate":
        return df.sort_values("return_3y",ascending=False).head(3)

    elif risk_level.lower()=="high":
        return df.sort_values("return_5y",ascending=False).head(3)

    else:
        return None
