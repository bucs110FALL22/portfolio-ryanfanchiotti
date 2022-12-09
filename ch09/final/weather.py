import requests

class Weather:
  def __init__(self,latitude,longitude):
    self.latitude = latitude
    self.longitude = longitude
    self.api_url = "https://api.open-meteo.com/v1/forecast?latitude="+str(self.latitude)+ "&longitude="+str(self.longitude)+"&current_weather=true"
    self.response = requests.get(self.api_url)
  def get(self):

    data = self.response.json()
    return data
  def getweather(self):
    
    weather = self.response.json()["current_weather"]
    return weather

