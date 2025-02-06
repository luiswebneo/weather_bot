import requests
from django.shortcuts import render

# Criando as views ao aplicar o conceito de MVC

def get_weather(request):
    api_key = 'sua chave'
    city = request.GET.get('city', 'São Paulo') # cidade padrão SP
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    data = response.json()

    if data['cod'] != 200:
        return jsonResponse({'error': 'Cidade não encontrada'}, {'error': data['message']}) 

    weather_data = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'rain': data.get('rain', {}).get('1h', 0),
        'wind_speed': data['wind']['speed'],
        'icon': data['weather'][0]['icon'],
    }

    return jsonResponse(weather_data)

    