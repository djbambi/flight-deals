"""This module provides functionality to query apis"""
import requests

TEQUILA_API_KEY = "RedUrHQDYp-aLuwJ-nuEzl-rC6Dt7lbe"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"


def get_iata_code(city):
    """
    Gets the IATA city code from the Tequila api.

    :param city: The city that needs an IATA code.
    :type city: string
    :return: IATA city code.
    :rtype: string
    """
    headers = {"apikey": TEQUILA_API_KEY}
    query = {"term": city}
    response = requests.get(
        url=f"{TEQUILA_ENDPOINT}/locations/query",
        headers=headers,
        params=query,
        timeout=5,
    )
    data = response.json()["locations"][0]["code"]
    return data
