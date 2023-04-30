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
        print(timeout_error)
        return "The request timed out"
    except requests.exceptions.HTTPError as http_error:
        print(http_error)
        return "The request returned an HTTP error"
    except requests.exceptions.SSLError as ssl_error:
        print(ssl_error)
        return "The request raised an SSL error"
    except requests.exceptions.ConnectionError as conn_error:
        print(conn_error)
        return "The request returned a connection error"
    except requests.exceptions.TooManyRedirects as redirect_error:
        print(redirect_error)
        return "The request produced too many redirects"
    except requests.exceptions.InvalidURL as url_error:
        print(url_error)
        return "The request has an invalid URL"
    except requests.exceptions.RequestException as gen_error:
        print(gen_error)
        return "The request raised a generic Exception"
    return response.json()
