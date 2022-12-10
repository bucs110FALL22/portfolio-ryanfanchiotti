import requests

class Weather:
  def __init__(self,latitude,longitude):
    '''
    initializes the classes' attributes
    args: (float) latitude, (float) longitude
    return: none
    '''
    self.latitude = latitude
    self.longitude = longitude
    self.api_url = "https://api.open-meteo.com/v1/forecast?latitude="+str(self.latitude)+ "&longitude="+str(self.longitude)+"&current_weather=true"
  def __str__(self) -> str:
    '''
    allows for easy access to url
    args: none
    return: (str) url of website data is grabbed from
    '''
    return self.api_url
  def get(self):
    '''
    grabs data from url
    args: none
    return: data from web api
    '''
    response = requests.get(self.api_url)
    data = response.json()
    return data
  def getweather(self):
    '''
    grabs current weather data from url
    args: none
    return: data from web api concerning current weather
    '''
    response = requests.get(self.api_url)
    weather = response.json()["current_weather"]
    return weather
