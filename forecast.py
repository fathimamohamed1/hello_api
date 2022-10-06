import os
import requests
from pprint import pprint
from datetime import datetime
import json

def get_w(wd):
    list_dict =[]
    for key in wd:
        #print(key, ":", key)
        d = dict(key)
        list_dict.append(d)
        pprint(d)
        print(list_dict[0]['main'] )
        print(list_dict[0]['description'])
    #print(list_dict[0])
        print(list_dict[0]['main'] )
        print(list_dict[0]['description'])

key =os.environ.get('WEATHER_KEY')

query={'q':'minneapolis,us','units':'imperial','appid':key}

url= 'https://api.openweathermap.org/data/2.5/forecast'

data= requests.get(url,params=query).json()
#pprint(data)

list_of_forecasts= data['list']


for forecast in list_of_forecasts:
    weather_description= forecast['weather']
    temp=forecast['main']['temp']
    timestamp=forecast['dt']
    forecast_date =datetime.fromtimestamp(timestamp) # i choose minnesota time becuase its more accurate to the local time compared to UTC which is the universal time and its also understood more.
    #wd = json.loads(weather_description)
    wd= weather_description
    #json_string = json.dumps(wd)
    #wd = json.loads(json_string)
    #print(type(wd))
    #pprint(wd)
    #w = f'{wd['main']} with {wd['description']}'
    print(f'At {forecast_date}the temperature is {temp}F and the weather is {wd}')
    

    


