import shodan

def get_apikey():
    api_key = open('api-key', 'r').read()
    print('Found stored api-key.')
    return api_key

apikey = get_apikey()
api = shodan.Shodan(apikey)

def search_hosts(hostlist=None):
    if hostlist is None:
        print('No host list was provided. Using the ./hostlist as a default one.')
        hostlist = open('hostlist').read()
    shodan_lookup = {}
    for host in hostlist:
        shodan_response = search(host)
        print(shodan_response)

def search(ip):
    host = api.host(ip)

    print('\n===========================================\n')
    print(f'IP: {host["ip_str"]}')
    print(f'Organization: {host.get("org", "n/a")}')
    print(f'Operationg System: {host.get("os", "n/a")}')

    for item in host['data']:
        print(f'Port: {item["port"]}')
        print(f'Banner:\n----\n{item["data"]}' + '\n-----\n')

    print('\n===========================================\n')
