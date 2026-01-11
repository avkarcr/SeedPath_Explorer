LEGACY_MODE = True  # False - for custom derivation path (non BIP44)

INPUT_FILE = "seeds.txt"
OUTPUT_FILE = "addresses.txt"

# Do not change unless you know what you are doing.
# Upper bounds for derivation loops.
# Note: values are used as range(limit), so the limit itself is NOT included.
limit_account = 5
limit_change = 1
limit_address = 5
