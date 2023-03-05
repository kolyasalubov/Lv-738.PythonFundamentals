import json
from operator import itemgetter

file_cars = open("cars.json", "r")
file_cars2 = open("cars2.json", "r")
result_file = open("result.json", "w")

# print(type(json.load(file_cars)))
res = json.load(file_cars)
res.append(json.load(file_cars2))
res.sort(key=itemgetter("max_speed"))

result_file.write(json.dumps(res))
file_cars.close()
file_cars2.close()
result_file.close()