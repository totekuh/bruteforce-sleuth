def save(dict):
    results = open('results', 'a', encoding='utf-8')

    for key, value in dict.items():
        print(f'{key}: {value}')

def geo_lookup():
    import requests
    import xml.etree.ElementTree as ET


    print('Enter IP address:')
    ip = input('> ')
    URL = f'http://api.geoiplookup.net/?query={ip}'

    response = requests.get(URL)

    if response.status_code == 200:
        root = ET.fromstring(response.text)

        print('\n====================================')
        geo_result = {}
        for child in root[0][0]:
            geo_result[child.tag.title()] = child.text
            # print(f'{child.tag.title()}: {child.text}')
        save(geo_result)
    else:
        print('Server returned not OK response, exiting.')
        exit(1)

geo_lookup()