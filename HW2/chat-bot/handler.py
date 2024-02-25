import json
import os
import requests
import re


def handle(req):
    try:
        data  = json.loads(req)
        regex = data['question']
        strings = ['name', 'time', 'figlet']
        value = ''
        for string in strings: 
            if re.match(regex, string):
                value = string 
                print(f'Matched: {string}')
                break
        
    except (KeyError, ValueError):
        return json.dumps({"error": "Invalid request payload"})

    url = f"http://127.0.0.1:8080/function/figlet"
    response = requests.get(url)
    if response.status_code != 200:
        return json.dumps({"error": "Error fetching weather data"})

    figlet_data = response.json()

    return json.dumps({"figlet": figlet_data})