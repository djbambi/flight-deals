"""This module provides functionality to query apis"""
import requests
import logging
import datetime

SHEETY_URL = "https://api.sheety.co/4a0d5dfd46da33d6c8aefcfae9f03882/fDeals/price"


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
        return response
    except requests.exceptions.HTTPError as http_error:
        return "There was an HTTP error - "


get_data_from_spreadsheet(SHEETY_URL)
