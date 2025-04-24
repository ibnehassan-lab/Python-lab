import json

try:
    with open('/Users/apple/python/customer.json', 'r') as f:
        data = json.load(f)
    print(data)
except json.JSONDecodeError as e:
    print("JSON Decode Error:", e)


