from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your own OpenWeatherMap API key
API_KEY = 'Y8e96a03be6f64383ba653923240210'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    
    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    # Make a request to OpenWeatherMap
    response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
    
    if response.status_code != 200:
        return jsonify({"error": "City not found"}), 404
    
    data = response.json()
    weather_info = {
        "city": data['name'],
        "temperature": data['main']['temp'],
        "description": data['weather'][0]['description'],
        "humidity": data['main']['humidity'],
        "wind_speed": data['wind']['speed']
    }
    
    return jsonify(weather_info)

if __name__ == '__main__':
    app.run(debug=True)
