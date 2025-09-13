from flask import Flask, jsonify, request
import pandas as pd
from generate_data import generate_data
from model import cluster_hotspots

app = Flask(__name__)

@app.route("/hotspots", methods=["GET"])
def hotspots():
    hour = int(request.args.get("hour", 18))
    df = generate_data(2000)  # generate fresh data
    df = cluster_hotspots(df)

    demand = df.groupby(['cluster', df['START_DATE'].dt.hour]).size().reset_index(name='ride_count')
    subset = demand[demand['START_DATE'] == hour].sort_values('ride_count', ascending=False).head(3)

    return jsonify(subset.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
