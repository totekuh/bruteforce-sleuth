import logging
import requests
import xml.etree.ElementTree as ET


def geo_lookup(ip):
    url = f'http://api.geoiplookup.net/?query={ip}'

    response = requests.get(url)

    try:
        if response.status_code == 200:
            root = ET.fromstring(response.text)
            geo_result = {}
            for child in root[0][0]:
                geo_result[child.tag.title()] = child.text
                # ISSUE with receiving '&' character literally (and probably others) in lookup response. Encoding?
            return geo_result
        else:
            logging.warning('Server returned not OK response, skipping.')
            return None
    except Exception as e:
        logging.warning(f'Something went wrong during {ip} lookup: {e}')
        return None
