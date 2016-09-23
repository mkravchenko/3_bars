import json


def load_data(filepath):
    file_to_read = open(filepath, 'r', encoding="utf-8")
    json_data = file_to_read.read()
    return json.loads(json_data)


def get_biggest_bar(data):
    biggest_value = float('-Inf')
    current_obj = None
    for fist_level in data:
        current_value = fist_level["Cells"]["SeatsCount"]
        if biggest_value < current_value:
            biggest_value = current_value
            current_obj = fist_level
    print(current_obj["Cells"]["Address"])
    return fist_level  # I can return the name of the biggest bar but in task nothing wrote about it


def get_smallest_bar(data):
    smallest_value = float('Inf')
    current_obj = None
    for fist_level in data:
        current_value = fist_level["Cells"]["SeatsCount"]
        if smallest_value > current_value:
            smallest_value = current_value
            current_obj = fist_level
    print(current_obj["Cells"]["Address"])
    return current_obj  # I can return the name of the smallest bar but in task nothing wrote about it


def get_closest_bar(data, longitude, latitude):
    difference_coord = None
    current_obj = None
    sum_smallest = float("Inf")
    longitude_diff_current = float("Inf")
    latitude_diff_current = float("Inf")
    for fist_level in data:
        coordinates = fist_level["Cells"]["geoData"]["coordinates"]
        longitude_current = coordinates[0]
        latitude_current = coordinates[1]
        if longitude_current == longitude and latitude_current == latitude:
            print(current_obj["Cells"]["Address"])
            return fist_level
        else:
            sum_of_current_coordins = (longitude_current + latitude_current)
            if abs(sum_of_current_coordins) <= sum_smallest:
                longitude_diff = longitude_current - longitude
                latitude_diff = latitude_current - latitude
                if longitude_diff_current > abs(longitude_diff) and latitude_diff_current > abs(latitude_diff):
                    longitude_diff_current = abs(longitude_diff)
                    latitude_diff_current = abs(latitude_diff)
                    current_obj = fist_level
                    difference_coord
    print(current_obj["Cells"]["Address"])
    return current_obj


if __name__ == '__main__':
    json_data = load_data("bars.json")
    get_biggest_bar(json_data)
    get_smallest_bar(json_data)
    # get_closest_bar(json_data, 37.7171150, 55.78262800012168)
    longitude = int(input("Next values only must be numeric types:\nlongitude: "))
    latitude = int(input("latitude: "))
    get_closest_bar(json_data, longitude, latitude)
