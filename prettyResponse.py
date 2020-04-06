import json

def prettyJsonResponseToText(x):
    x = json.loads(x.decode('utf-8'))
    for key in x:
        print(key, ':', x[key])