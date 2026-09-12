import requests


def get_api_data():
    url = "https://jsonplaceholder.typicode.com/users/6"

    try:
        response = requests.get(url)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:
        print("API request failed:", error)

        return None