import os, urllib.parse, urllib.request, json 
from flask import Flask, render_template, request, abort, Response
app = Flask(__name__)
OPEN_WEATHER_MAP_KEY = os.environ['OPEN_WEATHER_MAP_KEY']

@app.route('/forecast', methods=['GET'])
def get_weather():
  city = request.args.get('city')
  if city is None:
        abort(400, 'Missing argument city')
 

  data = {}
  data['q'] = city
  data['appid'] = OPEN_WEATHER_MAP_KEY
  data['units'] = 'imperial'
  data['cnt'] = 5
  url_values = urllib.parse.urlencode(data)
  url = 'http://api.openweathermap.org/data/2.5/forecast'
  full_url = url + '?' + url_values
  data = urllib.request.urlopen(full_url)

  resp = Response(data)
  resp.status_code = 200
  return render_template('weather_table.html', 
                         title='Weather App', 
                         data=json.loads(data.read().decode('utf8')))


@app.route('/', methods=['GET'])
def weather_search_page():  
  return render_template('index.html', title='Weather App')

app.run(host="0.0.0.0",port=8000)