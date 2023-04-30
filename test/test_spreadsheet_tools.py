from unittest.mock import Mock, patch
from requests.models import Response
import utils.spreadsheet_tools


@patch("utils.spreadsheet_tools.requests")
def test_get_request_returns_response(requests_mock):
    response = Response()
    response.status_code = 200
    response._content = b"Hello, World!"
    response.headers = {"Content-Type": "text/plain"}
    requests_mock.get.return_value = response
    assert (
        utils.spreadsheet_tools.get_data_from_spreadsheet("www.bbc.co.uk") == response
    )
