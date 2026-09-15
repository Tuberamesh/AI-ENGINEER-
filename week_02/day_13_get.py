import requests

url = "https://jsonplaceholder.typicode.com/users/5"

response = requests.get(url)

print(response)



url = "https://jsonplaceholder.typicode.com/users/5"
url = "https://example.com/users"

params = {
    "page": 2,
    "limit": 10
}
response = requests.get(url)

print(response.status_code)
print(response.text)