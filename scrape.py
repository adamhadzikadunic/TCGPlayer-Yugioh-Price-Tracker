
import requests

# tcgcsv
# 2 is the group number for Yugioh
url = "https://tcgcsv.com/tcgplayer/2/"

# header is needed according to API docs
# 24675 is the set for Chaos Origins as I test
r = requests.get(url=f"{url + '24675/products'}", headers={"User-Agent": "YGO Prices"})

print(r.json())

