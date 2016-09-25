import json
import sys
import math


def load_data(path_file):
    with open(path_file, 'r', encoding="utf-8") as f:
        read_data = f.read()
    return json.loads(read_data)


def get_biggest_bar(data):
    biggest_value = float('-Inf')
    current_obj = None
    for fist_level in data:
        current_value = fist_level["Cells"]["SeatsCount"]
        if biggest_value < current_value:
            biggest_value = current_value
            current_obj = fist_level
    return current_obj["Cells"]["Name"], current_obj["Cells"]["SeatsCount"]


def get_smallest_bar(data):
    smallest_value = float('Inf')
    current_obj = None
    for fist_level in data:
        current_value = fist_level["Cells"]["SeatsCount"]
        if smallest_value > current_value:
            smallest_value = current_value
            current_obj = fist_level
    return current_obj["Cells"]["Name"], current_obj["Cells"]["SeatsCount"]


def get_closest_bar(data, longitude_a, latitude_a):
    distance = float('Inf')
    jobject_to_return = None
    for fist_level in data:
        longitude_current, latitude_current = fist_level["Cells"]["geoData"]["coordinates"]
        distance_current = get_distance(longitude_current, latitude_current, longitude_a, latitude_a)
        if distance == distance_current:
            jobject_to_return = fist_level
            break
        else:
            if distance > distance_current:
                distance = distance_current
                jobject_to_return = fist_level
    return jobject_to_return["Cells"]["Name"], jobject_to_return["Cells"]["Address"], distance


def get_distance(longitude_b, latitude_b, longitude_a, latitude_a):
    return math.sqrt((longitude_b - longitude_a) ** 2 + (latitude_b - latitude_a) ** 2)


if __name__ == '__main__':
    path_to_file = sys.argv[1]
    json_data = load_data(path_to_file)
    biggest_bar = get_biggest_bar(json_data)
    smallest_bar = get_smallest_bar(json_data)

    print('The biggest bar name is: {0}, number of seats are: {1}'.format(biggest_bar[0], biggest_bar[1]))
    print('The smallest bar  name is: {0}, number of seats are: {1}'.format(smallest_bar[0], smallest_bar[1]))

    longitude = float(input("Next values must be numeric:\nlongitude: "))
    latitude = float(input("latitude: "))

    closest_bar = get_closest_bar(json_data, longitude, latitude)
    print('The closest bar name is "{0}", address is "{1}" and distance is: {2}'.format(closest_bar[0],
                                                                                        closest_bar[1],
                                                                                        closest_bar[2]))
