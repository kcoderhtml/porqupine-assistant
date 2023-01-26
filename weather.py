import requests

url = "https://wttr.in/?format=\"%t:+%C\""

response = requests.get(url)
print(response.text)

