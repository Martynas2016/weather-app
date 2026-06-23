from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

API_KEY = os.environ.get('WEATHER_API_KEY')
CITY = os.environ.get('CITY', 'Wroclaw')

@app.route('/')
def index():
    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    
    weather = {
        'city': CITY,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'feels_like': data['main']['feels_like']
    }
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
