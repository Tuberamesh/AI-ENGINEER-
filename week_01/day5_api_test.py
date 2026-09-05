# import requests

# # API URL
# url = "https://jsonplaceholder.typicode.com/users/1"

# # Send GET request
# response = requests.get(url)

# # 1. Print status code
# print("Status Code:", response.status_code)

# # 2. Print response headers
# print("\nResponse Headers:")
# print(response.headers)

# # 3. Convert JSON response into Python dictionary
# data = response.json()

# # 4. Print response body
# print("\nResponse Body:")
# print(data)

import requests

# API URL
url = "https://jsonplaceholder.typicode.com/users/99999"

# Send GET request
response = requests.get(url)

# 1. Print status code
print("Status Code:", response.status_code)

# 2. Print response headers
print("\nResponse Headers:")
print(response.headers)

# 3. Convert JSON response into Python dictionary
data = response.json()

# 4. Print response body
print("\nResponse Body:")
print(data)

