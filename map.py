import csv
import folium
from folium.plugins import MarkerCluster
import log_parser


def create_map():
    world = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)
    mc = MarkerCluster()
    with open(log_parser.csv_path, newline='') as csvfile:
        disconnections = csv.DictReader(csvfile)
        for d in disconnections:
            p = folium.Popup(f"{d['Isp']} {d['Ip']} {d['City']}, {d['Countrycode']}")
            folium.Marker((float(d['Latitude']), float(d['Longitude'])),
                          popup=p).add_to(mc)
    world.add_child(mc)
    world.save('map.html')
    print('map.html successfully created')


create_map()
