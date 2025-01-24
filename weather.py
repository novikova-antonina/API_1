import requests
a = ("https://wttr.in/Лондон?nTqmM&lang=ru",
"https://wttr.in/Шереметьево?nTqmM&lang=ru",
"https://wttr.in/Череповец?nTqmM&lang=ru")
for url in a:
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)