
'''API Key: AIzaSyCeqovBPCwT5vV-zNGEhi4cJbi2iT3ObZs'''

import requests
import json

# response = requests.get("https://www.googleapis.com/books/v1/volumes?q=search+terms")

# whatever key word you want to request from the api
request = "the"

# request the data and formats it
response = requests.get("https://www.googleapis.com/books/v1/volumes?q={}+inauthor".format(request))
formated_response = json.dumps(response.json() , indent=4)

# print(response.json())
print(formated_response)

