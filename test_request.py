import requests

data = {
    "tastes": ["spicy"],
    "location": [12.9719, 77.5937]
}

response = requests.post("http://127.0.0.1:5000/recommend", json=data)
print(response.json())
