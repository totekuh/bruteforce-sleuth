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

    for key, value in host.items():
        print(f'{key}: {value}')

    print('\n===========================================\n')
