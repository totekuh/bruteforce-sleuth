import re

def extract_ip_list(lines_to_skip=2):
    ip_list = []
    with open('log', 'r', encoding='utf-8') as f:
        for log in list(f):
            try:
                ip = re.search(r'(?<=Received disconnect from ).\S*', log).group(0)
                ip_list.append(ip)
            except Exception as e:
                None

    return ip_list

print(extract_ip_list())