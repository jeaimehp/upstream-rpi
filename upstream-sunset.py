#!/usr/bin/python3

import requests
import datetime

URL = "https://api.sunrise-sunset.org/json?lat=30.087479&lng=-97.169851&date=today&formatted=0"

## Ref: https://sunrise-sunset.org/api
## Usage limits and attribution
# The sunrise and sunset API can be used free of charge. You may not use this API
# in a manner that exceeds reasonable request volume, constitutes excessive or 
# abusive usage. We require that you show attribution to us with a link to our site.

r = requests.get(url = URL)
data = r.json()
sunset = datetime.datetime.strptime(data['results']['sunset'],'%Y-%m-%dT%H:%M:%S%z').time()
print(sunset.strftime('%H:%M'))
