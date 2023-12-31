"""
Utility functions for the application.

- fetch_data(code): Fetches data from the specified code using an API request.
- validate_create_book_req_data(request_data): Validates if the required fields are present in the request data.
"""

import requests

URL_BASE = "https://openlibrary.org{}.json"

def fetch_data(code):
    url = URL_BASE.format(code)
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-2xx status codes

    return response.json()

def validate_create_book_req_data(request_data):
    
    # Check if all the required fields are present in the request data
    if (
        "id" in request_data
        and "title" in request_data
        and "authors" in request_data
        and "works" in request_data
    ):
        for author in request_data["authors"]:
            if "id" not in author or "name" not in author:
                return False
        for work in request_data["works"]:
            if "id" not in work or "title" not in work:
                return False
        return True
    else:
        return False