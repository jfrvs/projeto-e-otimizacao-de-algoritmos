import pandas as pd
import random
from math import dist

# Define number of cities to be visited (deprecated)

NUMBER_OF_CITIES = 2009

def load_data(data='data.txt'):
    data = pd.read_csv(data, sep=' ', header=None)
    data.columns = ["X", "Y", "Cid"]
    return data

def calculate_total_distance(data):
    distance = 0
    
    for i in range(len(data) - 1):
        distance += dist([data.iloc[i, 0], data.iloc[i, 1]], [data.iloc[i + 1, 0], data.iloc[i + 1, 1]])
    
    return distance

def mutate1(data):
    first_spot = random.randint(0, len(data) - 1)
    second_spot = random.randint(0, len(data) - 1)

    pos1 = (first_spot, 0)
    pos2 = (second_spot, 0)

    temp = data.iat[pos1[0], pos1[1]]  # iat is faster for single cell access
    data.iat[pos1[0], pos1[1]] = data.iat[pos2[0], pos2[1]]
    data.iat[pos2[0], pos2[1]] = temp

    pos1 = (first_spot, 1)
    pos2 = (second_spot, 1)

    temp = data.iat[pos1[0], pos1[1]]  # iat is faster for single cell access
    data.iat[pos1[0], pos1[1]] = data.iat[pos2[0], pos2[1]]
    data.iat[pos2[0], pos2[1]] = temp

    pos1 = (first_spot, 2)
    pos2 = (second_spot, 2)

    temp = data.iat[pos1[0], pos1[1]]  # iat is faster for single cell access
    data.iat[pos1[0], pos1[1]] = data.iat[pos2[0], pos2[1]]
    data.iat[pos2[0], pos2[1]] = temp

    return data

def mutate2(data):
    segment_size = 11
    initial_pos = random.randint(0, len(data) - 12)
    
    pos = []

    for i in range(segment_size):
        pos.append(initial_pos + i)

    for i, el in enumerate(pos):
        first_spot = pos[i]
        second_spot = pos[i] + segment_size

        pos1 = (first_spot, 0)
        pos2 = (second_spot, 0)

        temp = data.iat[pos1[0], pos1[1]]  # iat is faster for single cell access
        data.iat[pos1[0], pos1[1]] = data.iat[pos2[0], pos2[1]]
        data.iat[pos2[0], pos2[1]] = temp

        pos1 = (first_spot, 1)
        pos2 = (second_spot, 1)

        temp = data.iat[pos1[0], pos1[1]]  # iat is faster for single cell access
        data.iat[pos1[0], pos1[1]] = data.iat[pos2[0], pos2[1]]
        data.iat[pos2[0], pos2[1]] = temp

        pos1 = (first_spot, 2)
        pos2 = (second_spot, 2)

        temp = data.iat[pos1[0], pos1[1]]  # iat is faster for single cell access
        data.iat[pos1[0], pos1[1]] = data.iat[pos2[0], pos2[1]]
        data.iat[pos2[0], pos2[1]] = temp
    return pos

def run():
    data = load_data()
    distance = calculate_total_distance(data)

    while True:
        print(f"Current distance: {distance}")
        for i in range(100):
            new_data = mutate1(data)
            new_dist = calculate_total_distance(new_data)
            if new_dist < distance:
                distance = new_dist
                data = new_data
data = load_data()
print(mutate2(data))
