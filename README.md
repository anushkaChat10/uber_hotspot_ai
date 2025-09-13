# 🚖 Uber Hotspot Recommendation AI
Ride-hailing platforms face a key challenge: matching driver supply with passenger demand. Drivers often waste valuable time cruising without passengers, while riders wait longer than expected during peak times. This imbalance creates inefficiency and lost revenue opportunities.

This project was built with the motivation to minimize driver idle time and improve rider availability by recommending demand hotspots. Instead of relying on historical Uber datasets (which are not always publicly available), the system generates synthetic ride data and simulates weather conditions and city events to model real-world demand dynamics.

The objective is to create an AI-powered recommendation system that predicts when and where ride demand will surge, and to serve these insights interactively through maps and APIs for real-time use.

✅ Solution Approach

Our solution combines multiple AI and data science techniques into one pipeline:

Synthetic Data Generation – create realistic ride request data with timestamps, locations, and zones, enriched with simulated weather and event effects.

Hotspot Clustering – use KMeans and DBSCAN to identify high-demand zones and adapt to both dense and irregular demand clusters.

Demand Forecasting – apply Facebook’s Prophet model to predict ride request trends by time of day and week.

Context Integration – adjust hotspot strength using simulated weather conditions and special events (e.g., concerts, sports games).

Visualization – generate interactive maps with hotspots, heatmaps, and forecast plots.

Real-Time Recommendation API – deliver actionable suggestions to drivers or platforms for practical deployment.

🔍 Why This Matters

For Drivers: Spend less time idle, more time earning.

For Riders: Faster pickups and shorter wait times.

For Platforms: Higher efficiency and optimized fleet distribution.

## 🔧 Setup
```bash
git clone https://github.com/YOUR_USERNAME/uber-hotspot-ai.git
cd uber-hotspot-ai
pip install -r requirements.txt
```

## ▶️ Run
Generate synthetic data + map:
```bash
python generate_data.py
```

Launch real-time API:
```bash
python app.py
```

Open [http://127.0.0.1:5000/hotspots](http://127.0.0.1:5000/hotspots) to see live recommendations.

---

## 📊 Output
- `map.html`: Hotspot heatmap  
- Forecast plots per zone  
- API returns JSON with top hotspots  

---

## 🛠 Tech Stack
- Python (Pandas, NumPy, Scikit-learn, Prophet)
- Folium (maps)
- Flask (API)
- DBSCAN, KMeans (clustering)
