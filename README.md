# 🚖 Uber Hotspot Recommendation AI

An AI-powered system to recommend Uber driver hotspots using:
- Synthetic ride data (no external datasets required)
- Weather & event simulation
- Clustering (KMeans + DBSCAN)
- Prophet demand forecasting
- Real-time recommendation API

---

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
