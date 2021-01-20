from youtube_app import app
import requests
import unittest

BASE = "http://127.0.0.1:5000/"

data = [
    {"name": "tutorial", "views": 500, "likes": 10},
    {"name": "tutorial_2", "views": 980, "likes": 28},
    {"name": "tutorial_3", "views": 155500, "likes": 535}
]

for i in range(len(data)):
    response = requests.put(BASE+"video/"+str(i), data[i])
    print(response.json)

# Try to GET a video that does not exist, should abort
response = requests.get(BASE+"video/6")
print(response.json())

# Try a PATCH to change the name of video 0
response = requests.patch(BASE+"video/0", {"name": "tutorial_update"})
print(response.json())

# Try a DELETE to change the name of video 0
response = requests.delete(BASE+"video/2")
print(response.status_code)

def add_two_numbers(a, b):
    return a + b

class TestClass():
    def test_add_two_numbers_pass(self):
        assert add_two_numbers(5, 10) == 15
    
    def test_add_two_numbers_fail(self):
        assert add_two_numbers(5, 10) != 10

class FlaskTestCase(unittest.TestCase):
    def test_get(self):
        pass

if __name__ == "__main__":
    unittest.main()