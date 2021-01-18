import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"name": "tutorial", "views": 500, "likes": 10},
    {"name": "tutorial_2", "views": 980, "likes": 28},
    {"name": "tutorial_3", "views": 155500, "likes": 535}
]

for i in range(len(data)):
    response = requests.put(BASE+"video/"+str(i), data[i])
    print(response.json)

# Attempt to put a video, but it is missing required args
response = requests.put(BASE+"video/3", {"likes": 10})
print(response.json())

# Put a correct video
response = requests.put(BASE+"video/3", {"name": "tutorial_4", "views": 30, "likes": 2})
print(response.json())

# Get that correct video you just put above
response = requests.get(BASE+"video/0")
print(response.json())

# Try to put a video that already exists, should abort
response = requests.put(BASE+"video/0", data[0])
print(response.json())

# Try to get a video that does not exist, should abort
response = requests.get(BASE+"video/6")
print(response.json())

# Try to delete a video that does not exist, should abort
response = requests.delete(BASE+"video/6")
print(response.json())

# Delete a video that does exist
response = requests.delete(BASE+"video/1")
print(response)
