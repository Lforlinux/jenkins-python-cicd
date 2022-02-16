from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return 'App Works! Use /employee to fetch employee details'

@app.route('/employee', methods=['GET'])
def employee():
    url = 'http://dummy.restapiexample.com/api/v1/employees'
    response = requests.get(url=url,headers={'User-Agent': 'curl/7.54.0'})
    data = response.json()
    return data

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)