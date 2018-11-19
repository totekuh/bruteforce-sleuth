def geo_lookup():
    import requests
    import xml.etree.ElementTree as ET


    print('Enter IP address:')
    ip = input('> ')
    URL = f'http://api.geoiplookup.net/?query={ip}'

    geo_response = requests.get(URL)

    if geo_response.status_code == 200:
        root = ET.fromstring(geo_response.text)

        print('\n====================================')
        for child in root[0][0]:
            print(f'{child.tag.title()}: {child.text}')
    else:
        print('Server returned not OK response, exiting.')
        exit(1)

geo_lookup()