import folium, requests

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
data = requests.get(url).json()

m = folium.Map(location=[20,0], zoom_start=2)

for feature in data["features"]:
    coords = feature["geometry"]["coordinates"]
    mag = feature["properties"]["mag"]
    folium.CircleMarker(
        location=[coords[1], coords[0]],
        radius=mag*2,
        popup=f"Magnitude: {mag}",
        color="red"
    ).add_to(m)

m.save("earthquake_map.html")
print("Map saved as earthquake_map.html")
