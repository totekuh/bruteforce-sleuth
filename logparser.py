import re


ip_rgx = r'(?<=Received disconnect from ).\S*'


def extract_ip_list():
    ip_list = []
    with open('log', 'r', encoding='utf-8') as f:
        for log in list(f):
            try:
                ip = re.search(ip_rgx, log).group(0)
                ip_list.append(ip)
            except Exception as e:
                None

    return set(ip_list)


print(extract_ip_list())