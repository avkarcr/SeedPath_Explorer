from bip_utils import (
    Bip39SeedGenerator,
    Bip44,
    Bip44Coins,
    Bip44Changes
)

def get_legacy_addresses(seed: str) -> list:

        try:
            seed_bytes = Bip39SeedGenerator(seed).Generate()
            bip44 = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM)
            addr = (
                bip44
                .Purpose()
                .Coin()
                .Account(0)
                .Change(Bip44Changes.CHAIN_EXT)
                .AddressIndex(0)
                .PublicKey()
                .ToAddress()
            )
            return [addr]
        except Exception as e:
            return [f"ERROR: {e}"]
