import json
import os
import requests
import re
from time import gmtime, strftime


def handle(req):
    #Get the data from user side
    try:
        data  = json.loads(req)
        query = data['question'].lower()
    except (KeyError, ValueError):
        return json.dumps({"error": "Invalid request payload"})
    
    #Build the result for the query from a user
    result = {}
    if re.search(r'name', query):
        result = {"name" : "chatbot"}
    elif re.search(r'time', query):
        result = {"time" : strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())}
    else:
        url = f"http://127.0.0.1:8080/function/figlet"
        response = requests.get(url)
        if response.status_code != 200:
            return json.dumps({"error": "Error fetching weather data"})

        print(json.loads(response.json()))
        result = {"figlet" : json.loads(response.json())}
        
    #Return
    return json.dumps(result)