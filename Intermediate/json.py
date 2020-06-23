import simplejson as json
import os


ages = "./ages.json"
if os.path.isfile(ages) and os.stat(ages).st_size != 0:
    old_file = open(ages, "r+")
    data = json.loads(old_file.read())
    print("Current age is", data["age"], "-- adding a year.")
    data["age"] = data["age"] + 1
    print("New age is", data["age"])

else:
    old_file = open(ages, "w+")
    data = {"name": "Nobert", "age": 24}
    print("No file fault, setting default age to", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))


