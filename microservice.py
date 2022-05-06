from flask import Flask, request
import requests
import apikey

app = Flask(__name__)


@app.route("/health")
def health():
    return {"health": "server up and running!"}


@app.route("/coordinates")
def coordinates():
    apiKey = apikey.key
    city = request.args.get('city', '')
    if not city:
        res = {"error": "no city provided"}
        return res

    apiURL = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={apiKey}"
    req = requests.request('GET', apiURL)

    if len(req.json()) == 0:
        return {"error": "city not found"}

    cityData = req.json()
    returnData = {
        "city": cityData[0]["name"],
        "country": cityData[0]["country"],
        "lat": cityData[0]["lat"],
        "lon": cityData[0]["lon"]
    }

    if "state" in cityData[0]:
        returnData["state"] = cityData[0]["state"]
        
    return returnData


if __name__ == "__main__":
    app.run(debug=True)
