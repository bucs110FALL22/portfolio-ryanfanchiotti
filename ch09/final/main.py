from weather import Weather
from location import Location
from sunrisesunset import SunriseSunset

def main():
  ip = input("Please input the IPv4 address you'd like to see the weather and sunrise/sunset time of: ")
  location = Location(ip)
  longitude = location.getlongitude()
  latitude = location.getlatitude()
  weather = Weather(latitude,longitude)
  currentweather = weather.getweather()
  temp = currentweather['temperature']
  ws = currentweather['windspeed']
  wd = currentweather['winddirection']
  print("This is the current weather for the location of that ip address: Temperature -> "+str(temp)+" Celsius, Wind Speed -> "+str(ws)+" KM/H, Wind Direction -> "+str(wd)+" Degrees")
  sunrisesunset = SunriseSunset(latitude,longitude)
  srt = sunrisesunset.getsunrise()
  sst = sunrisesunset.getsunset()
  print("Today's sunrise for the location of that ip address happens at "+str(srt)+" GMT, and sunset happens at "+str(sst)+" GMT")
  

main()