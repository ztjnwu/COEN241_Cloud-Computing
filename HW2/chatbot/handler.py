import json
import os
import re
from time import gmtime, strftime
import subprocess
import requests


def handle(req):
    #Get the data from user side
    data  = json.loads(req)

    #Build the result for the query from a user
    result = {}
    if 'question' in data:
        query = data['question']
        if re.search(r'name', query):
            result = "chatbot"
        elif re.search(r'time', query):
            result = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        else:
            result = {"error": "Invalid request payload"}

    elif 'figlet' in data:
        query = data['figlet']
        url = f'http://10.62.0.5:8080/function/figlet'
        response = requests.post(url, data=query)
        result = response.text
    
    else:
        result = {"error": "Invalid request payload"}
		
	#Print
    print(result)

    #Return
    return
    #return json.dumps(result)



if __name__ == "__main__":
    
    req = '{"question": "name"}'
    handle(req)
    #result = handle(req)
    #print(json.loads(result), "\n")

    req = '{"question": "time"}'
    handle(req)
    #result = handle(req)
    #print(json.loads(result), "\n")

    req = '{"figlet": "Great!"}'
    handle(req)
    #result = handle(req)
    #print(json.loads(result))
    
    
    
    

