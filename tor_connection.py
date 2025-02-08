import requests

proxies = {"http": "socks5h://127.0.0.1:9050", "https": "socks5h://127.0.0.1:9050"}


def check_tor_connection():
    print("Tor Connection Check")
    try:
        system_ip = requests.get("https://ident.me", proxies=proxies).text
        tor_ip_list = requests.get("https://check.torproject.org/exit-addresses").text
        if system_ip in tor_ip_list:
            print("Tor_IP: ", system_ip)
            print("Tor Connection Success")
        else:
            print("Tor Connection Failed")
    except requests.RequestException:
        print("Error: Configure Tor as service")
        print("For quick setup refer: https://miloserdov.org/?p=1839")
        exit()
