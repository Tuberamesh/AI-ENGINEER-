from dotenv import load_dotenv
import os

load_dotenv()

# 1. API KEY
api_key = os.getenv("API_KEY")

if api_key is None:
    print("API key is missing")
else:
    print("API key found")


# 2. FILE
try:
    with open("sample.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")


# 3. USER INPUT
try:
    number = int(input("Enter a number: "))
    print("Number:", number)

except ValueError:
    print("Please enter a valid number")