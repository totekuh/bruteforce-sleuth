import log_parser
import folium
from folium.plugins import MarkerCluster


def create_map():
    disconnections = log_parser.parse()

    try:
        world = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)
        mc = MarkerCluster()
        for d in disconnections:
            p = folium.Popup(f"{d.geo['Isp']} {d.geo['Ip']} {d.geo['City']}, {d.geo['Countrycode']}")
            folium.Marker((float(d.geo['Latitude']), float(d.geo['Longitude'])),
                          popup=p).add_to(mc)
        world.add_child(mc)
        world.save('map.html')
        print('map.html successfully created')
    except Exception as e:
        print(f'Error creating map: {e}')


create_map()
