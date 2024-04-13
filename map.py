import folium

map = folium.Map(location=[9.7, 7.29], zoom_start=6 , tile_layer="Stamen Terrain")

#Adding Feature Group
fg= folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[9.088184, 7.408628], popup="This is where you work", icon= folium.Icon(color='green')))
map.add_child(fg)

map.save('Map1.html')
