from colorama import Fore, Style
from tor_connection import check_tor_connection
from height_mainnet import check_mempool_height
from height_testnet import check_testnetmempool_height
from onion_urls import check_onion_urls
from onion_blocks import check_onion_blocks

if __name__ == "__main__":
    check_tor_connection()

    print(f"\n{Fore.YELLOW} CHECKING URLS {Style.RESET_ALL}")
    check_onion_urls("/Users/anon/Desktop/IT/2025/Tor/Dojo_mainnet.txt")
    check_onion_urls("/Users/anon/Desktop/IT/2025/Tor/Dojo_testnet.txt")

    print(f"\n{Fore.YELLOW} CHECKING MEMPOOL BLOCKS {Style.RESET_ALL}")
    check_mempool_height()
    check_onion_blocks("/Users/anon/Desktop/IT/2025/Tor/blocks_mainnet.txt")
    check_testnetmempool_height()
    check_onion_blocks("/Users/anon/Desktop/IT/2025/Tor/blocks_testnet.txt")
