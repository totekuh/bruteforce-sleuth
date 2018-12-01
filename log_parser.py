from collections import Counter
import geoip
import logging
import re

#logging.basicConfig(level=logging.INFO)
rgx = r'(?<=Received disconnect from )(?P<ip>.\S*).*: (?P<response>.*)(?= \[preauth)'


class DisconnectionLog:
    def __init__(self, log, ip, response):
        self.raw = log
        self.ip = ip
        self.response = response
        self.geo = geoip.geo_lookup(self.ip)
        logging.info(f"New disconnection {self.ip} from {self.geo}: {self.response}")


def parse():
    disconnections = []
    with open('log', 'r', encoding='utf-8') as f:
        for log in list(f):
            try:
                m = re.search(rgx, log)
                ip = m.group('ip')
                response = m.group('response')
                dlog = DisconnectionLog(log, ip, response)
                if dlog.geo is not None:
                    disconnections.append(dlog)
            except AttributeError:
                logging.debug(f'Not interested in line: {log}')
                pass
    return disconnections
