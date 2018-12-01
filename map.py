import log_parser
import folium
import logging
from collections import Counter


class Map:
    def __init__(self):
        disconnections = log_parser.parse()
        locations = [(float(d.geo['Latitude']), float(d.geo['Longitude'])) for d in disconnections]
        self.markers = Counter(locations)

        self.map = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)
        for loc in self.markers:
            popup = f'Unique IPs: {self.markers[loc]}'
            folium.Marker(loc, popup=popup).add_to(self.map)
        self.map.save('map.html')


m = Map()
