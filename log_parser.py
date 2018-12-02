import csv
import geoip
import re

rgx = r'(?<=Received disconnect from )(?P<ip>.\S*).*: (?P<response>.*)(?= \[preauth)'
log_path = 'log'
csv_path = 'disconnections.csv'

class DisconnectionLog:
    def __init__(self, log, ip, response):
        self.raw = log
        self.ip = ip
        self.response = response
        self.geo = geoip.geo_lookup(self.ip)
        print(f"New disconnection {self.ip} from {self.geo}: {self.response}")


def parse():
    disconnections = []
    with open(log_path, 'r', encoding='utf-8') as f:
        for log in list(f):
            try:
                m = re.search(rgx, log)
                ip = m.group('ip')
                response = m.group('response')
                dlog = DisconnectionLog(log, ip, response)
                if dlog.geo is not None:
                    disconnections.append(dlog)
            except AttributeError:
                pass

    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['Ip', 'Host', 'Isp', 'City', 'Countrycode', 'Countryname', 'Latitude', 'Longitude']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows([d.geo for d in disconnections])
        print(f'Saved {len(disconnections)} log events as {csv_path}')
    return disconnections

parse()