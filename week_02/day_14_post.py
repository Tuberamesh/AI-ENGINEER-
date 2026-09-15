import requests

url = "https://jsonplaceholder.typicode.com/posts"

name = input("Enter your name: ")
email = input("Enter your email: ")
role = input("Enter your role: ")

data = {
    "name": name,
    "email": email,
    "role": role
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(
    url,
    json=data,
    headers=headers
)

print("Status:", response.status_code)
print("Response:", response.json())