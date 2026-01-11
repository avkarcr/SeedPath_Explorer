import unicodedata


def normalize_seed(seed: str) -> str:
    seed = unicodedata.normalize("NFKD", seed)
    seed = " ".join(seed.strip().split())
    return seed
