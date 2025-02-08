import requests
from colorama import Fore, Style


def check_mempool_height():
    url = "https://mempool.space/api/blocks/tip/height"
    try:
        response = requests.get(url)
        block_height = response.text
        print(
            f"{Fore.CYAN}Current Mainnet Bitcoin block height: {block_height}{Style.RESET_ALL}"
        )
    except requests.RequestException:
        print("Error fetching mainnet block height")
