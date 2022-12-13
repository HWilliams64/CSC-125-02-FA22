import requests

phase = input("Please type a sentence to translate: ")
source_lang = input("Please type a language of the sentence: ")
target_lang = input("Please type a language to translate to: ")

url = "https://libretranslate.de/translate"
data = {"q":phase, "source":source_lang, "target":target_lang}

response = requests.post(url, data=data)
translation = response.json()['translatedText']
print(f"{phase} -> {translation}")
