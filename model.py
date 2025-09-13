import pandas as pd
from sklearn.cluster import KMeans, DBSCAN
from prophet import Prophet
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def cluster_hotspots(df, method="kmeans", n_clusters=5):
    coords = df[['Lat', 'Lon']]
    if method == "dbscan":
        clustering = DBSCAN(eps=0.01, min_samples=10).fit(coords)
        df['cluster'] = clustering.labels_
    else:
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        df['cluster'] = kmeans.fit_predict(coords)
    return df

def forecast_zone(df, zone, test_days=2):
    ts = (
        df[df['START'] == zone]
        .groupby(df['START_DATE'].dt.floor('h'))
        .size()
        .reset_index(name='y')
    )
    ts.columns = ['ds', 'y']

    if len(ts) < test_days * 24:
        return None

    train = ts.iloc[:-test_days*24]
    test = ts.iloc[-test_days*24:]

    model = Prophet(daily_seasonality=True, weekly_seasonality=True)
    model.fit(train)
    future = model.make_future_dataframe(periods=test_days*24, freq='h')
    forecast = model.predict(future)

    compare = forecast[['ds', 'yhat']].merge(test, on='ds', how='left').dropna()
    mae = mean_absolute_error(compare['y'], compare['yhat'])
    rmse = np.sqrt(mean_squared_error(compare['y'], compare['yhat']))

    return mae, rmse, compare, forecast
