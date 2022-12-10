import requests

class Location:
  def __init__(self,ip):
    '''
    initializes the classes' attributes
    args: (str) ip
    return: none
    '''
    self.ip = str(ip)
    self.api_url = "https://api.ipgeolocation.io/ipgeo?apiKey=2086b4ea9201489fa8b8202f94b0316c&ip=" + self.ip
  def get(self):
    '''
    grabs data from url
    args: none
    return: data from web api
    '''
    response = requests.get(self.api_url)
    data = response.json()
    return data
  def getlatitude(self):
    '''
    grabs latitude data from url
    args: none
    return: data from web api concerning latitude
    '''
    response = requests.get(self.api_url)
    latitude = response.json()["latitude"]
    return latitude
  def getlongitude(self):
    '''
    grabs longitude data from url
    args: none
    return: data from web api concerning longitude
    '''
    response = requests.get(self.api_url)
    longitude = response.json()["longitude"]
    return longitude


  