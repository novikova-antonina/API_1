import requests


def send_request(city):
    payload = {"n":"","T":"","q":"","M":"","lang": "ru"}  
    response = requests.get(f'https://wttr.in/{city}', params=payload) 
    print(response.url)
    response.raise_for_status()  
    return response.text

def main():
    cities = ('Лондон', 'Шереметьево', 'Череповец')  
    
    for city in cities:
        weather_info = send_request(city)
        print(f"Погода в {city}:\n{weather_info}\n")

if __name__ == '__main__':
    main()
