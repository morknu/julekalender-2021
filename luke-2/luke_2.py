import io
import csv
import haversine as hs
from math import radians, cos, sin, asin, sqrt


def distance(pt1, pt2):
    return hs.haversine(pt1, pt2)


def closest(pt, others):
    return min(others, key=lambda i: distance(pt, i))


def get_locations():
    csv_file = io.open('cities.csv', mode='r', encoding='utf-8')
    csv_reader = csv.DictReader(csv_file)
    _locations = set()
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            s = row['location']
            res = tuple(reversed(tuple(map(float, s[s.find("(") + 1:s.find(")")].split(' ')))))
            _locations.add(res)
        line_count += 1
    return _locations


north_pole = (90.0, 0.0)

# Get locations
locations = get_locations()

# Start at the North Pole
current_location = north_pole
total_distance = 0

# Santa's journey
while len(locations) > 0:
    next_location = closest(current_location, locations)
    current_distance = distance(current_location, next_location)
    total_distance += current_distance
    print(current_location, next_location, current_distance)
    current_location = next_location
    locations.remove(next_location)

# Get back to the North Pole
current_distance = distance(current_location, north_pole)
total_distance += current_distance

print(current_location, north_pole, current_distance)
print('Total travel-distance for Santa(km): ', int(round(total_distance)))
