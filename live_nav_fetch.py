import requests
import pandas as pd

scheme_codes = [
    "125497",
    "119551",
    "120503",
    "118632",
    "119092",
    "120841"
]

for code in scheme_codes:
    try:
        url = f"https://api.mfapi.in/mf/{code}"

        response = requests.get(url, timeout=30)

        response.raise_for_status()

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        nav_df.to_csv(
            f"data/raw/{code}_nav.csv",
            index=False
        )

        print(f"{code} saved successfully")

    except Exception as e:
        print(f"Failed for {code}: {e}")