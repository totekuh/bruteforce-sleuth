import geoip
import logparser

addresses = logparser.extract_ip_list(open('log', 'r').read())

for ip in addresses:
	print(f'Performing IP lookup for the IP address: {ip}')
	geoip.geo_lookup(ip=ip.replace('\n', ''))
