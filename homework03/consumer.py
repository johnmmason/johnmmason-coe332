#!/bin/python3
import requests
import pprint

if __name__ == '__main__':
    # POPULATE THE DATASET
    requests.get(url="http://localhost:5018/generate_animals?num_animals=200")
    
    # MAKE AN API REQUEST:
    # Choose a request by uncommenting the corresponding line.

    # response = requests.get(url="http://localhost:5018/animals")
    response = requests.get(url="http://localhost:5018/animals?num_animals=5")
    # response = requests.get(url="http://localhost:5018/animals?num_animals=1&head_type=snake")

    # PRINT THE RESPONSE
    pprint.pprint(response.json(), compact=False)
