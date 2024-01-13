import requests
from modules.terminal_tools import *

# Gets data from the API using the requests library


def get_api_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print_error("Unable to fetch data")
        return None
