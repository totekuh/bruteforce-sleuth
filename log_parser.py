import re
import geoip

rgx = r'(?<=Received disconnect from )(?P<ip>.\S*).*: (?P<response>.*)(?= \[preauth)'

# Do we need a parent class Log to track other logs or do we just look for brute-force attempt logs?


class DisconnectLog:
    def __init__(self, log, ip, response):
        self.raw = log
        self.ip = ip
        self.response = response
        self.location = geoip.geo_lookup(self.ip)
        print(f'Disconnected {self.ip} from {self.location}: {self.response}')


def extract_ip_list():
    disconnections = []
    with open('log', 'r', encoding='utf-8') as f:
        for log in list(f):
            try:
                m = re.search(rgx, log)
                ip = m.group('ip')
                response = m.group('response')
                dl = DisconnectLog(log, ip, response)
                disconnections.append(dl)
            except Exception as e:
                None

    return disconnections


extract_ip_list()