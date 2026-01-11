from hdwallet import HDWallet
from hdwallet.cryptocurrencies import Ethereum
from hdwallet.mnemonics import BIP39Mnemonic
from hdwallet.derivations import BIP44Derivation

from utils import normalize_seed
from config import limit_account, limit_change, limit_address


def get_bip44_addresses(seed: str) -> list:

    normalized = normalize_seed(seed)
    mnemonic = BIP39Mnemonic(normalized)

    addresses = []

    wallet = HDWallet(cryptocurrency=Ethereum)
    wallet.from_mnemonic(mnemonic)

    for account in range(0, limit_account):
        for change in range(0, limit_change):
            for address in range(0, limit_address):
                wallet.clean_derivation()
                derivation = BIP44Derivation(
                    account=account,
                    change=change,
                    address=address
                )
                wallet.from_derivation(derivation)
                # path = f"m/44'/60'/{account}'/{change}/{address}"
                # print(path, wallet.address())
                addresses.append(wallet.address())
    return addresses
