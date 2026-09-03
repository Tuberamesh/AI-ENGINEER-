# This is a sample code to demonstrate API testing using the requests library in Python.
#get method
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1",
)

print(response.status_code)
print(response.json())
print(response.headers)



# post method
import requests

response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json={
        "id": 1,
        "name": "John Doe",
        "username": "johndoe",
        "email": "john.doe@example.com"
    }
)

print(response.status_code)
print(response.json())


# put method
data = {
    "name": "Ramesh",
    "username": "decoder"
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/users/3",
    json=data
)

print(response.status_code)
print(response.json())




import requests

response = requests.delete(
    "https://jsonplaceholder.typicode.com/users/3"
)

print(response.status_code)
print(response.json())