import folium

mapA = folium.Map([7.872, 80.401], zoom_start=8, title="Test Map")
fg = folium.FeatureGroup(name="Volcanoes")
fg.add_child(folium.Marker(location=[7.872, 80.401], popup="Home", icon=folium.Icon(color="red")))

mapA.add_child(fg)
mapA.save("test.html")
