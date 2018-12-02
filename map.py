import csv
import folium
from collections import Counter


class Mapper:
    def __init__(self, map_type):
        self.map_type = map_type

        if self.map_type == 'map':
            self.marking_method = folium.Marker
            self.data = self.load_csv()
        elif self.map_type == 'map-clustered':
            self.marking_method = folium.CircleMarker
            locations = [(float(d['Latitude']), float(d['Longitude'])) for d in self.load_csv()]
            self.data = Counter(locations)
            # add counting

        self.name = f'{self.map_type}.html'
        print(self.data)

    def load_csv(self):
        with open('disconnections.csv', 'r', newline='') as csv_file:
            disconnections = csv.DictReader(csv_file)
            return [d for d in disconnections]

    def generate(self):
        try:
            world = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)
            marking_args = {}

            for d in self.data:
                if self.map_type == 'map':
                    marking_args['location'] = float(d['Latitude']), float(d['Longitude'])
                    marking_args['popup'] = folium.Popup(f"{d['Isp']} {d['Ip']} {d['City']}, {d['Countrycode']}")
                elif self.map_type == 'map-clustered':
                    marking_args['location'] = d
                    marking_args['radius'] = self.data[d] / 2
                    marking_args['popup'] = folium.Popup(f'Attempts: {self.data[d]}')

                self.marking_method(**marking_args).add_to(world)

            world.save(self.name)
            print(f'{self.name} successfully created')
        except Exception as e:
            print(f'Error creating {self.name}: {e}')


m1 = Mapper('map')
m1.generate()

m2 = Mapper('map-clustered')
m2.generate()
