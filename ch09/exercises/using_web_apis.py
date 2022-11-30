import requests

url = 'https://meowfacts.herokuapp.com/'

def main():
  r = requests.get(url)
  j = r.json()
  print(j)


