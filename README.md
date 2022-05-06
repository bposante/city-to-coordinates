# City to GeoCoordinates Microservice

A microservice that returns the coordinates of the specified city.

**Install Dependencies**

`pip install -r requirements.txt`

OR

`pip3 install -r requirements.txt`

---

**Add API Key**

Get your API key from https://home.openweathermap.org/api_keys.  

Paste your key into the file apikey.py where specified.

---

**Start Microservice**

Navigate to the directory that contains microservice.py.

`python microservice.py`

OR

`python3 microservice.py`

---

**How to call API**

Make an HTTP GET request to http://localhost:5000/coordinates?city={requested_city}  

Example: http://localhost:5000/coordinates?city=toronto

Returns a JSON object with the city, country, state (if applicable), latitude, and longitude.

    `Return Object = {  
        "city": city name,
        "country": country name,  
        "lat": city latitude,  
        "lon": city longitude,  
        "state": city state if applicable  
    }`

In the case of an error, the API will return a JSON object with an error key and a message containing the reason for the error.