import geoip, logparser
import folium

# Make an empty map
m = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)

ip_list = logparser.extract_ip_list()
for ip in ip_list:
    try:
        lat, lon = geoip.geo_lookup(ip)
        print(lat, lon)
        folium.Marker([lat, lon]).add_to(m)
    except:
        print(f'cannot handle {ip}')

m.save('map.html')
