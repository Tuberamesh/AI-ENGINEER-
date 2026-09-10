import requests

url = "https://jsonplaceholder.typicode.com/users?id=6"


response = requests.get(url)

print("Status Code:", response.status_code)

users = response.json()

for user in users:
    print(
        user["name"],
        "|",
        user["email"],
        "|",
        user["company"]["name"]
    )