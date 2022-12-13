import requests
  
url = "https://dog-api.kinduff.com/api/facts"
#     "https://dog-api.kinduff.com/api/facts?number=1&raw=True"

while True:
    data = {"number": 1, "raw": "true"}
    response = requests.get(url, params=data)

    if response.ok:
        print(f"Fact: {response.text}")
    else: 
        print(f"Something went wrong, please try again. Status code: {response.status_code}")
    
    ui = input("Would you like to hear another fact? [y/n]: ")
    if ui.lower().strip() in ("no", "n"):
        break