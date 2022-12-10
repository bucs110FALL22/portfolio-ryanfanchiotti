import requests

class SunriseSunset:
  def __init__(self,latitude,longitude):
    '''
    initializes the classes' attributes
    args: (float) latitude, (float) longitude
    return: none
    '''
    self.latitude = latitude
    self.longitude = longitude
    self.api_url = "https://api.sunrise-sunset.org/json?lat="+str(latitude)+"&lng="+str(longitude)
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
  def getsunrise(self):
    '''
    grabs sunrise time data from url
    args: none
    return: data from web api concerning sunrise time
    '''
    response = requests.get(self.api_url)
    results = response.json()["results"]
    sunrisetime = results["sunrise"]
    return sunrisetime
  def getsunset(self):
    '''
    grabs sunset time data from url
    args: none
    return: data from web api concerning sunset time
    '''
    response = requests.get(self.api_url)
    results = response.json()["results"]
    sunsettime = results["sunset"]
    return sunsettime



  