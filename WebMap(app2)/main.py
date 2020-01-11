import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
volcano_type = list(data["TYPE"])
elev = list(data["ELEV"])

_map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

html = """<h4>
    Volcano Information:<br>
    Height: %s m<br>
    Type: %s<br>
    </h4>"""


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


fg = folium.FeatureGroup(name="MyMap")
for lt, ln, vt, el in zip(lat, lon, volcano_type, elev):
    iframe = folium.IFrame(html=html % (str(elev), vt), width=200, height=100)
    fg.add_child(
        folium.CircleMarker(location=(lt, ln), popup=folium.Popup(iframe), radius=10, fill=True, fill_opacity=0.7,
                            color='grey', fill_color=color_producer(el)))

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding="utf-8-sig").read(), style_function=lambda x: {
    'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties'][
        'POP2005'] < 20000000 else 'red'}))
_map.add_child(fg)

_map.save("Map1.html")
