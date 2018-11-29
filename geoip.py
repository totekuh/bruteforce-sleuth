import requests
import xml.etree.ElementTree as ET


def save(dict):
    # with open('results', 'a', encoding='utf-8') as f:
    # results = do_whatever()

    for key, value in dict.items():
        print(f'{key}: {value}')


def geo_lookup(ip=None):

    if ip is None:
        print('Enter IP address:')
        ip = input('> ')
    url = f'http://api.geoiplookup.net/?query={ip}'

    response = requests.get(url)

    try:
        if response.status_code == 200:
            root = ET.fromstring(response.text)
            geo_result = {}
            for child in root[0][0]:
                geo_result[child.tag.title()] = child.text
            # save(geo_result)
            return float(geo_result['Latitude']), float(geo_result['Longitude'])
        else:
            print('Server returned not OK response, skipping.')
            return
    except:
        return
