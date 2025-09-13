import folium
from folium.plugins import HeatMap

def build_map(df, cluster_centers=None, output_file="map.html"):
    map_center = [df['Lat'].mean(), df['Lon'].mean()]
    m = folium.Map(location=map_center, zoom_start=12)

    if cluster_centers is not None:
        for i, center in enumerate(cluster_centers):
            folium.Marker(location=center, popup=f"Hotspot {i}").add_to(m)

    HeatMap(data=df[['Lat', 'Lon']].values, radius=8, max_zoom=13).add_to(m)
    m.save(output_file)
    return m
