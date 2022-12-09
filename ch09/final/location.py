import requests

class Location:
  def __init__(self,ip):
    self.ip = ip
    self.api_url = "https://api.ipgeolocation.io/ipgeo?apiKey=2086b4ea9201489fa8b8202f94b0316c&ip=" + self.ip
    self.response = requests.get(self.api_url)
  def get(self):

    data = self.response.json()
    return data
  def getlatitude(self):
    
    latitude = self.response.json()["latitude"]
    return latitude
  def getlongitude(self):
    
    longitude = self.response.json()["longitude"]
    return longitude


  