#!/usr/bin/python3
import datetime
import sys
from calendar import monthrange
import requests
from dateutil import tz

if len(sys.argv)==1: sys.exit("Year not found. USAGE: ./year-localtz-sunrise-sunset-creator.py YYYY")

year = sys.argv[1]

def days_cur_month(m):
    y = int(year)
    m = int(m)
    ndays = monthrange(y,m)
    monthList = []
    for d in range(1,int(ndays[1])+1):
        print (d)
        dateObject = datetime.date(y, m, d)
        print (dateObject.strftime('%Y-%m-%d'))
        monthList.append(dateObject.strftime('%Y-%m-%d'))
    return(monthList)

def utc_localtime(datetimeObject):
  from_zone = tz.gettz('UTC')
  to_zone = tz.tzlocal()
  datetimeObject = datetimeObject.replace(tzinfo=from_zone)
  central = datetimeObject.astimezone(to_zone)
  print("Was {} now {}".format(datetimeObject.strftime('%m/%d/%Y %I:%M %p'),central.strftime('%m/%d/%Y %I:%M %p')))
  return(central.strftime('%I:%M %p')) 

def sunrise_sunset(dateList):
  
  #Test URL for API
  URL = "https://api.sunrise-sunset.org/json?lat=30.087479&lng=-97.169851&date=today&formatted=0"

  ## Ref: https://sunrise-sunset.org/api
  ## Usage limits and attribution
  # The sunrise and sunset API can be used free of charge. You may not use this API
  # in a manner that exceeds reasonable request volume, constitutes excessive or
  # abusive usage. We require that you show attribution to us with a link to our site.
  for dayDate in dateList: 
    URL = "https://api.sunrise-sunset.org/json?lat=30.087479&lng=-97.169851&date={}&formatted=0".format(dayDate)
    r = requests.get(url = URL)
    data = r.json()
    sunset = datetime.datetime.strptime(data['results']['sunset'][0:19],'%Y-%m-%dT%H:%M:%S')
    sunrise = datetime.datetime.strptime(data['results']['sunrise'][0:19],'%Y-%m-%dT%H:%M:%S')
    print (URL)
    print (utc_localtime(sunrise))
    print("{} {} {}".format(sunrise.strftime('%m/%d/%Y'),utc_localtime(sunrise),utc_localtime(sunset)))

for month in range(12):
  sunrise_sunset(days_cur_month(month + 1))
