import requests
import datetime
import calendar

URL = "https://api.sunrise-sunset.org/json?lat=30.087479&lng=-97.169851&formatted=0&date="

## Ref: https://sunrise-sunset.org/api
## Usage limits and attribution
# The sunrise and sunset API can be used free of charge. You may not use this API
# in a manner that exceeds reasonable request volume, constitutes excessive or
# abusive usage. We require that you show attribution to us with a link to our site.

r = requests.get(url = URL)
data = r.json()
cal = calendar.Calendar()
for month in range(1,13):
    for date in cal.itermonthdates(2021, month):
        check = URL + str(date)
        r = requests.get(url = check)
        data = r.json()
        sunrise = datetime.datetime.strptime(data['results']['sunrise'][0:19],'%Y-%m-%dT%H:%M:%S')
        sunset = datetime.datetime.strptime(data['results']['sunset'][0:19],'%Y-%m-%dT%H:%M:%S')
        
        print ('{} {} {}'.format(sunrise.strftime('%m/%d/%Y'),sunrise.strftime('%I:%M %p'),sunset.strftime('%I:%M %p')))
        #print(date)
