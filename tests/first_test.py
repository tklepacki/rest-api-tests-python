from pytest_steps import test_steps
import requests
from config.urls import Urls

@test_steps('test_first')
def test_get_user_request():
    session = requests.session()
    response = session.get(Urls.BASE_URL)
    
    assert (response.status_code == 200), f"Status Code validation failed for {response.request.url}"
    yield