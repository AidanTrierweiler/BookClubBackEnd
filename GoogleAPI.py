
'''API Key: AIzaSyCeqovBPCwT5vV-zNGEhi4cJbi2iT3ObZs'''

import requests

response = requests.get("https://www.googleapis.com/books/v1/volumes?q=search+terms")
print(response.json())