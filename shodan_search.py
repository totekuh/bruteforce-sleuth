import shodan

def get_apikey():
    api_key = open('api-key', 'r').read()
    print('Found stored api-key.')
    return api_key

def search_hosts(hostlist=None):
    shodan_lookup = {}
    if hostlist is None:
        print('No host list was provided. Using the ./hostlist as a default one.')
        hostlist = open('list', 'r', newline='\n').read().split('\n')
    for host in hostlist:
        shodan_response = search(host)
        shodan_lookup[host] = shodan_response

    return shodan_lookup

def search(ip):
    host = api.host(ip)
    print('\n===========================================\n')
    for key, value in host.items():
        print(f'{key}: {value}')
    print('\n===========================================\n')
    return host


apikey = get_apikey()
api = shodan.Shodan(apikey)
search_hosts()