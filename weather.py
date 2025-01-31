import requests


def request_weather(city):
    payload = {"n":"","T":"","q":"","M":"","lang": "ru"}  
    response = requests.get(f'https://wttr.in/{city}', params=payload) 
    response.raise_for_status()  
    return response.text

def main():
    cities = ('Лондон', 'Шереметьево', 'Череповец')  
    
    for city in cities:
        weather_info = request_weather(city)
        print(f"Погода в {city}:\n{weather_info}\n")

if __name__ == '__main__':
    main()