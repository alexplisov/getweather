from flask import Flask, send_file, request
import requests

app = Flask(__name__)

@app.route("/")
def get_weather():
    city = request.args.get('city')
    if not city:
        return 'Use city parameter to clarify your request.'
    return requests.get(f"https://wttr.in/{city}?format=1").content

