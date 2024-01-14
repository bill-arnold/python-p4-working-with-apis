import requests
import json

class GetPrograms:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_response_body(self):
        response = requests.get(self.api_url)
        return response.content

    def load_data(self):
        return self.get_response_body()

if __name__ == "__main__":
    # Replace the API endpoint with the actual URL from the API documentation
    api_url = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
    
    programs = GetPrograms(api_url)
    response_body = programs.load_data()

    print(response_body.decode('utf-8'))
