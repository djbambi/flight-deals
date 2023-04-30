"""Data manager module"""


def get_city_and_id_for_empty_iata(sheet_data):
    """
    Extracts city and id from sheet data where the IATA code cell is empty.

    :param sheet_data: The data from the spreadsheet.
    :type sheet_data: json
    :return: Cities and id that have missing IATA codes.
    :rtype: list of dictionaries
    """
    city_and_id = []
    for iata in sheet_data:
        if iata["iataCode"] == "":
            city_and_id.append({"city": iata["city"], "id": iata["id"]})
    return city_and_id
