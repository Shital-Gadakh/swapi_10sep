""""
Task
The star wars API lists 82character in stra wars series.
for the task we have to create a random number generator.This random number generater
should fetch numbers between 1-82.using these random number we have to fetch random
15 characters from API using 'requests' lib
"""


import random


def produce_character(start=1, stop=82):
    return (random.randrange(1, stop=82) for item in range(1, 16))


obj = produce_character()
for i in range(1, 16):
    print(next(obj))

print(__name__)