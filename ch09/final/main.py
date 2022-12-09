from weather import Weather
from location import Location

def main():
  ip = input("Please input the IPv4 address you'd like to see the weather of: ")
  location = Location(ip)
  longitude = location.getlongitude()
  latitude = location.getlatitude()
  weather = Weather(latitude,longitude)
  currentweather = weather.getweather()
  print("This is the current weather for that ip address: "+str(currentweather))

main()