import requests


def get_tor_ip_list():
    data = requests.get('https://check.torproject.org/exit-addresses')

    data_req = data.text.split()
    exit_ip_addresses = []

    for x in data_req:
        if(x == "ExitAddress"):
            index = data_req.index(x)
            exit_ip_addresses.append(data_req[index+1])
    return exit_ip_addresses

def check_ip(query,exit_ip_addresses):
    for ip in exit_ip_addresses:
        if (ip == query):
            return True
    return False

def main():
    print("Getting Tor exit ip address list...")
    exit_ip_address = get_tor_ip_list()
    print("Enter the ip address to check:")
    query = input()
    if(check_ip(query, exit_ip_address) == True):
        print("Yes  this is an exit node.")
    else:
        print("No this is not an exit node.")

if __name__ == "__main__":
    main()

