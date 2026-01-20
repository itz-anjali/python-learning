import requests

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)

response = requests.get('https://www.google.com')

print(response.status_code) #  (200 means YES)


# Ek fake API se user ka data maanga
r = requests.get('https://jsonplaceholder.typicode.com/users/1')

if r.status_code == 200:
    # .json() use karke hum seedha dictionary bana lete hain
    data = r.json() 
    print(f"User ka naam hai: {data['name']}")
    print(f"User ka email hai: {data['email']}")
else:
    print("Koi gadbad ho gayi!")