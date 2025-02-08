import requests
from colorama import Fore, Style


def check_testnetmempool_height():
    url = "https://mempool.space/testnet4/api/blocks/tip/height"
    try:
        response = requests.get(url)
        testnetblock_height = response.text
        print(
            f"{Fore.CYAN}Current Testnet Bitcoin block height: {testnetblock_height}{Style.RESET_ALL}"
        )
    except requests.RequestException:
        print("Error fetching testnet block height")
