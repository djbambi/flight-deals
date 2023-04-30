"""This module provides functionality to query apis"""
import requests


def get_data_from_spreadsheet(url):
    """
    Fetches data from a google sheet.

    :param url: The sheety url that correspods to the Google sheet.
    :type url: string
    :return: Google sheet values.
    :rtype: json
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.Timeout as timeout_error:
        return f"The request timed out - {timeout_error}"
    except requests.exceptions.HTTPError as http_error:
        print(f"The request returned an HTTP error - {http_error}")
    except requests.exceptions.SSLError as ssl_error:
        print(f"The request raised an SSL error - {ssl_error}")
    except requests.exceptions.ConnectionError as conn_error:
        print(f"The request returned a connection error - {conn_error}")
    except requests.exceptions.TooManyRedirects as redirect_error:
        print(f"The request produced too many redirects - {redirect_error}")
    except requests.exceptions.InvalidURL as url_error:
        print(f"The request has an invalid URL - {url_error}")
    except requests.exceptions.RequestException as gen_error:
        print(f"The request raised a generic Exception - {gen_error}")
    return response.json()


def put_data_to_spreadsheet(url, updated_data):
    """
    Puts IATA codes into spreadsheet.

    :param url: The sheety url that correspods to the Google sheet.
    :param updated_data: IATA code for corresponding city.
    :type url: string
    :type updated_data: string
    :return: Google sheet values.
    :rtype: json
    """
    request_data = {"price": {"iataCode": updated_data}}

    try:
        response = requests.put(url, json=request_data, timeout=5)
        response.raise_for_status()
    except requests.exceptions.Timeout as timeout_error:
        print(f"The GET request timed out - {timeout_error}")
    except requests.exceptions.HTTPError as http_error:
        print(f"The GET request returned an HTTP error - {http_error}")
    except requests.exceptions.SSLError as ssl_error:
        print(f"The GET request raised an SSL error - {ssl_error}")
    except requests.exceptions.ConnectionError as conn_error:
        print(f"The GET request returned a connection error - {conn_error}")
    except requests.exceptions.TooManyRedirects as redirect_error:
        print(f"The GET request produced too many redirects - {redirect_error}")
    except requests.exceptions.InvalidURL as url_error:
        print(f"The GET request has an invalid URL - {url_error}")
    except requests.exceptions.RequestException as gen_error:
        print(f"The GET request raised a generic Exception - {gen_error}")
    return response.json()
