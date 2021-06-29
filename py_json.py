# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON

userJSON = '{"first_name": "Alphonse", "last_name": "Brandon", "Age": 40}'


# Parse to dict
user = json.loads(userJSON)