import requests

def make_request(query_parameters):
    base_url = "https://api.nasa.gov/neo/rest/v1/feed?";
    response = requests.get(base_url + query_parameters, timeout = 60);
    return response;
