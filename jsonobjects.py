import json

person = {
    "name": "Sunil",
    "age": 25,
    "city": "Pune",
    "hasChildren": True,
    "titles": ["programmar", "husband", "engineer"],
}

# Convert the above python object to JSON object
personJSON = json.dumps(person, indent=4)
print(personJSON)

# Write the python object to JSON File
with open("person.json", "w") as file:
    json.dump(person, file, indent=4)
    file.close

# Read JSON object in python dictionary object
loadedprsn = json.loads(personJSON)
print(loadedprsn)

# Read JSON file in python object
with open("person.json", "r") as file:
    loadedper = json.load(file)
    print(loadedper)


# JSON from a class object


class User:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


# Create another class for checking error
class UserNew:
    def __init__(self, name, age, sex) -> None:
        self.name = name
        self.age = age
        self.sex = sex


user = User("Sunil Bidgar", 27)
newuser = UserNew("New Bidgar", 2, "Male")

# Write a custom encoder to convert class to json
def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object " + o.__class__.__name__ + " is not JSON serializable")


userJSON = json.dumps(user, default=encode_user)
print(userJSON)

# This generates the Type error as raised above
# userJSON = json.dumps(newuser, default=encode_user)

# --- Use JSON encoder class to encode the object
from json import JSONEncoder


class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)


userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)

# Directly using UserEncoder
userJSON = UserEncoder().encode(user)
print(userJSON)

# Consvert json object to class type


def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct["name"], age=dct["age"])
    return dct


user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)
