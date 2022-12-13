import requests

phrases = input("Please type in a sentence to be translated: ")
#source_language = input("Please type in the language of the source: ") 
target_language = input("Please type in the language to be translated to: ")

detect_url = "https://libretranslate.de/detect"
detect_data = {"q": phrases}

response = requests.post(url=detect_url, data=detect_data)
source_language = response.json()[0]["language"]
 
url = "https://libretranslate.de/translate"
data = {"q": phrases, "source":source_language, "target":target_language}

response = requests.post(url=url, data=data)
translation = response.json()['translatedText']
print(f"{phrases} -> {translation}")
