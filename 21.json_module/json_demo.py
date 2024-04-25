"""
    JavaScript Object Notation
    
    Type translation mapping from JSON to Python
    https://docs.python.org/3/library/json.html#encoders-and-decoders

"""

import json

PEOPLE_STRING = """
{
    "people":[
        {
            "name":"John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com","john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name":"John Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true        
        }
    ]

}
"""

# load json string into python object using json.loads() method
data = json.loads(PEOPLE_STRING)
print("type of data:", type(data))
print("type of people:", type(data["people"]))
print("\naccess the data:", data)

# access the person in a People List
print("\naccess the person in a People List:")
for person in data["people"]:
    print(person)

print("\naccess the person name only:")
for person in data["people"]:
    print(person["name"])
    # delete phone key from the object
    del person["phone"]

# dump a python object into a json string using json.dumps() method
# use indent arugment to format the json
# use sort_keys argument to sort each key in alphabetically
print("\nremove phone number from the list and put it back to json:")
NEW_STRING = json.dumps(data, indent=2, sort_keys=True)
print(NEW_STRING)


# load json file into python object and write objects back to JSON file
with open(
    "C:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\21.json_module\\states.json",
    "r",
    encoding="UTF-8",
) as f:
    data = json.load(f)

for state in data["states"]:
    print(state["name"], state["abbreviation"])
    del state["area_codes"]

with open(
    "C:\\Users\\chin.p.ho\\Documents\\Python Tutorial\\21.json_module\\new_states.json",
    "w",
    encoding="UTF-8",
) as f:
    json.dump(data, f, indent=2)
