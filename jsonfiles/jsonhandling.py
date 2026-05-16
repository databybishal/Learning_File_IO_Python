# Lesson: JSON - Javascript Object Notation.

# Text Format : Storing and transporting data.
# Self describing and easy to understand.
# JSON is used to send data between computers.
# JSON is language independent.
# Example:

# key-value pairs: '{"name": "John", "age": 25, "height": 6}'

# Parse the json to java script object. Readability increases.

# We have built-in library: json

# First

# Convert the normal data into json file and dump into json file

import json  # first have to import json modules
myDict = {
    "people": [
        {
            "name": "bishal",
            "age": 23,
            "height": 5.6
        },
        {
            "name": "komal",
            "age": 22,
            "height": 5.5
        },
        {
            "name": "sujan",
            "age": 24,
            "height": 5.3
        }

    ]
}

# dumps
# By only using dumps the everything is written in one line so have to indent better use 2 or 4 for proper spacing
# It will conver the dict in json and dump in this string
json_string = json.dumps(myDict, indent=4, sort_keys=True)


with open("jsonfiles/my_data.json", 'w') as file:  # putting the json file into my_data.json
    json.dump(myDict, file, indent=4)

with open("jsonfiles/my_data2.json", 'w') as file:
    file.write(json_string)

# How to read the data from the json file

# first always import the built-in json modules

# reading the data from json file
data = {"theme": "dark", "version": 1.0}
with open("jsonfiles/my_data.json", 'r') as file:
    data.update(json.load(file))
print(data)
print(type(data))


data2 = {"theme": "dark", "version": 1.0}
with open("jsonfiles/my_data.json", 'r') as file:
    data2.update(json.loads(json_string))
print(data2)
print(type(data2))
print(data2['people'][0]['name']) # extracting the value from dict


