import geocoder
import random
import folium
from sklearn.ensemble import IsolationForest  



### Fetching and simulating realistic GPS data
#simulate grabbing 10 different gps locations around my current locale
location = geocoder.ip('me')
base_lat, base_lng = location.latlng


gps_points = []

for _ in range(10):
    #added some random movement to mock walking and moving around
    lat = base_lat + random.uniform(-0.0005, 0.0005)
    lng = base_lng + random.uniform(-0.0005, 0.0005)
    #this will add the gps points as a pair to each index
    gps_points.append((lat,lng))


gps_points.append((base_lat + 0.05, base_lng + 0.05))

#####



myMap =folium.Map(location=gps_points[0], zoom_start=15)

for point in gps_points:
    folium.Marker(point).add_to(myMap)


folium.PolyLine(gps_points, color= "blue").add_to(myMap)

myMap.save("gps_path.html")
print("Map has been saved as gps_path.html")



X = gps_points
model = IsolationForest(contamination=0.1)
labels = model.fit_predict(X)

print("Outlier GPS points:")
for idx, label in enumerate(labels):
    if label == -1:
        print(gps_points[idx])