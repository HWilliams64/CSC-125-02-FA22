import gdown
import json
import random

output = "./jokes.json"
url = "https://drive.google.com/file/d/1JcQhNqbntQFBrRZE2gtxdnQzEt8BjBpX/view?usp=share_link"
gdown.download(url=url, output=output, quiet=True, fuzzy=True)

with open(output, 'r') as file:
    jokes = json.load(file)
    joke = random.choice(jokes)
    print(f"{joke['q']}\n{joke['a']}")