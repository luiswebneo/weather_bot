import logging
from telegram import Update
from telegram.ext import Update, CommandHandler, CallBackContext
import requests

# configuração do logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# função para buscar 
def start(city):
    api_key = 'sua_chave_api_aqui'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    update.message.reply_text('Olá! Eu sou o bot do tempo. Digite /tempo <cidade> para saber o tempo.')


    if data['cod'] !=200:
        return None

    weather_data = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'rain': data.get('rain', {}).get('1h', 0),
        'wind_speed': data['wind']['speed'],
    }

    return weather_data

# comando /start

def clima(update: Update, context: CallBackContext) -> None:
    city = ' '.join(context.args)
    weather_data = start(city)

    if not weather_data:
        update.message.reply_text('Cidade não encontrada. Tente novamente.')
        return
    
    message = (
        f"Clima em {weather_data['city']}:\n"
        f"Temperatura: {weather_data['temperature']}°C\n"
        f"Descrição: {weather_data['description']}\n"
        f"Umidade: {weather_data['humidity']}%\n"
        f"Chuva: {weather_data['rain']} mm\n"
        f"Velocidade do vento: {weather_data['wind_speed']} m/s\n"
    )

def main() -> None:
    updater = Updater("SEU_TOKEN_AQUI")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("clima", clima))

    updater.start_polling()
    updater.idle()
    if __name__ == '__main__':
        main()
    # comando /clima


