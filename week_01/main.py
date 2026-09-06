import requests

user_id = input("Enter user ID: ")

url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    name = data["name"]
    email = data["email"]
    city = data["address"]["city"]

    print("User Information")
    print("----------------")
    print("Name:", name)
    print("Email:", email)
    print("City:", city)

else:
    print("❌ User not found")