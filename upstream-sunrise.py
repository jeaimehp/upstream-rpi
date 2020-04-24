#!/usr/bin/python3

import requests
URL = "https://api.sunrise-sunset.org/json?lat=30.43602752685547&lng=-97.68285369873047&date=today"

r = requests.get(url = URL)
data = r.json()

print(data['results']['sunrise'])
