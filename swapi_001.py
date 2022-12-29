""""
Task
The star wars API lists 82character in strawars series.
for the task we have to create a random number generator.This random number generater
should fetch numbers between 1-82.using these random number we have to fetch random
15 characters from API using 'requests' lib
"""
import requests
import requests as requests

from utils.randgen import produce_characters

start = 1
stop = 15

obj = produce_characters()
characters = []

for i in range(start, stop + 1):
    characters.append(next(obj))

home_url = "https://swapi.dev"
relative = "/api/people/{0}"

for num_ in characters:
    absolute_url = home_url + relative.format(num_)
    print(f"fetching details using -{absolute_url}")
    response = requests.get(absolute_url)
    response = response.json()
    print(response)
    print("######" * 25)

if __name__ == "__main__":
    print("current module getting executed")