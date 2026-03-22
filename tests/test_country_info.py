from pytest_steps import test_steps

import xml.etree.ElementTree as ET

import services.country_info as country_info

@test_steps('test_get_capital_city_request')
def test_get_capital_city_request():
    capital_city_response = country_info.get_capital_city("PL")


    assert (capital_city_response.status_code == 200), f"Status Code validation failed for {capital_city_response.request.url}"
    
    root = ET.fromstring(capital_city_response.content)
    namespace = {"m": "http://www.oorsprong.org/websamples.countryinfo"}

    assert (root.find(".//m:CapitalCityResult", namespace).text == "Warsaw"), f"Capital city validation failed for {capital_city_response.request.url}"

    yield
