import requests
r = requests.get('http://localhost:5700/dosomething?x=3&y=7')

print(r.text)