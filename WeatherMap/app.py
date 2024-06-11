from flask import Flask, render_template, request
import requests

app = Flask(__name__)
api_key = 'YOUR_API_KEY'  # 여기에 OpenWeatherMap API 키를 입력하세요.

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
    else:
        weather = None
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
