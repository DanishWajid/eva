import requests
import json
import feedparser
import datetime


class Knowledge(object):
    def __init__(self, _current_user, local):
        self.current_user = _current_user
        self.apiurl = "https://evaapi12.localtunnel.me" if not local else "http://127.0.0.1:5000"


    def find_weather(self):

        lat = 33.684420
        lon = 73.047885

        weather_req_url = "https://api.darksky.net/forecast/%s/%s,%s" % ("dafddca65618d5947f1a23f2f3f51ecf", lat, lon)
        r = requests.get(weather_req_url)
        weather_json = json.loads(r.text)

        temperature = int(weather_json['currently']['temperature'])

        current_forecast = weather_json['currently']['summary']
        wind_speed = int(weather_json['currently']['windSpeed'])

        return {'temperature': temperature, 'windSpeed': wind_speed, 'current_forecast': current_forecast}

    def get_news(self):
        
        url = ('https://newsapi.org/v2/top-headlines?'
        'country=us&'
        'category=technology&'
        'apiKey=ff33f4d1d2c1455eafcb410bef3a2375')

        response = requests.get(url)
        news_dict = json.loads(response.content)["articles"]
        headlines = []
        count  = 0
        for newz in news_dict:
            headlines.append(newz["title"])
            count += 1
            if count == 5:
                break

        return headlines

        # return ret_headlines

    def todo(self):
        print("getting todo:",self.apiurl + "/todo/get")
        r = requests.get(self.apiurl + "/todo/get")
        resp = json.loads(r.text)
        toReturn = []
        for note in resp["todos"]:
            toReturn.append(note[1])
        return toReturn

    def note(self):
        print("getting note:",self.apiurl + "/note/get")
        r = requests.get(self.apiurl + "/note/get")
        resp = json.loads(r.text)
        toReturn = []
        for note in resp["notes"]:
            toReturn.append(note[3])
        return toReturn


    def add_user(self, user_obj):
        print("adding user")
        r = requests.get(self.apiurl + "/user/add/"+user_obj._super+"&"+user_obj._face+"&"+user_obj.username+"&"+user_obj.username+"&"+user_obj.password)

    def set_alarm(self, alarmtime):
        print("setting alarm")
        r = requests.get(self.apiurl + "/alarm/add/"+alarmtime+"&"+str(self.current_user._id))

    def find_currency(self):   

        # Where pkr is the base currency you want to use
        url = 'https://v3.exchangerate-api.com/bulk/fe12dc4317270c8c24e99e6a/PKR'

        # Making our request
        response = requests.get(url)
        data = response.json()

        # Your JSON object
        print (data)

    def get_map_url(self, location, map_type=None):
        if map_type == "satellite":
            return "http://maps.googleapis.com/maps/api/staticmap?center=%s&zoom=13&scale=false&size=1200x600&maptype=satellite&format=png" % location
        elif map_type == "terrain":
            return "http://maps.googleapis.com/maps/api/staticmap?center=%s&zoom=13&scale=false&size=1200x600&maptype=terrain&format=png" % location
        elif map_type == "hybrid":
            return "http://maps.googleapis.com/maps/api/staticmap?center=%s&zoom=13&scale=false&size=1200x600&maptype=hybrid&format=png" % location
        else:
            return "http://maps.googleapis.com/maps/api/staticmap?center=%s&zoom=13&scale=false&size=1200x600&maptype=roadmap&format=png" % location



