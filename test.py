import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE+"hello/ian")
print(response.json())

# response = requests.post(BASE+"hello/ian")
# print(response.json())