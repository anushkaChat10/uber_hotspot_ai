import pandas as pd
import numpy as np

def generate_data(n_samples=5000):
    np.random.seed(42)

    start_date = pd.to_datetime("2023-01-01")
    end_date = pd.to_datetime("2023-01-15")
    date_range = pd.date_range(start=start_date, end=end_date, freq="min")

    timestamps = np.random.choice(date_range, n_samples)
    lats = np.random.uniform(40.6, 40.9, n_samples)
    lons = np.random.uniform(-74.05, -73.75, n_samples)
    zones = np.random.choice(["Manhattan", "Brooklyn", "Queens"], n_samples)

    # Weather + Events (synthetic)
    weather = np.random.choice(["Clear", "Rain", "Snow"], n_samples, p=[0.7, 0.2, 0.1])
    events = np.random.choice(["None", "Concert", "Sports"], n_samples, p=[0.8, 0.1, 0.1])

    df = pd.DataFrame({
        "START_DATE": timestamps,
        "START": zones,
        "Lat": lats,
        "Lon": lons,
        "Weather": weather,
        "Event": events
    })

    return df

if __name__ == "__main__":
    df = generate_data()
    print("Sample Data:")
    print(df.head())
    df.to_csv("synthetic_rides.csv", index=False)
