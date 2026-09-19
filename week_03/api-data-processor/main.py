from api import fetch_data
from processor import process_data
import json

def save_data(data):
    with open("result.json", "w") as file:
        json.dump(data, file, indent=4)

def main():
    data = fetch_data()

    if data is None:
        return


    processed_data = process_data(data)

    print(processed_data)
    save_data(processed_data)


if __name__ == "__main__":
    main()