from pytest_steps import test_steps

import xml.etree.ElementTree as ET

import services.part_04.country_info as country_info

@test_steps('test_get_full_country_info_request')
def test_get_full_country_info_request():
    full_country_info_response = country_info.get_full_country_info('PL')

    assert (full_country_info_response.status_code == 200), f"Status Code validation failed for {full_country_info_response.request.url}"

    root = ET.fromstring(full_country_info_response.content)
    namespace = {'m': 'http://www.oorsprong.org/websamples.countryinfo'}
    
    assert (root.find('.//m:sISOCode', namespace).text == "PL"), "ISO Code verfication failed"
    assert (root.find('.//m:sName', namespace).text == "Poland"), "Name verfication failed"
    assert (root.find('.//m:sCapitalCity', namespace).text == "Warsaw"), "Capital City verfication failed"
    assert (root.find('.//m:sPhoneCode', namespace).text == "48"), "Phone Code verfication failed"
    assert (root.find('.//m:sContinentCode', namespace).text == "EU"), "Contintent Code verfication failed"
    assert (root.find('.//m:sCurrencyISOCode', namespace).text == "PLN"), "Currency ISO Code verfication failed"
    assert (root.find('.//m:sCountryFlag', namespace).text == "http://www.oorsprong.org/WebSamples.CountryInfo/Flags/Poland.jpg"), "Country Flag verfication failed"
    assert (root.find('.//m:tLanguage', namespace).find('.//m:sISOCode', namespace).text == "pol"), "Language ISO Code verfication failed"
    assert (root.find('.//m:tLanguage', namespace).find('.//m:sName', namespace).text == "Polish"), "Language Name verfication failed"

    yield

@test_steps('test_get_capital_city_request')
def test_get_capital_city_request():
    capital_city_response = country_info.get_capital_city('PL')

    assert (capital_city_response.status_code == 200), f"Status Code validation failed for {capital_city_response.request.url}"
    
    root = ET.fromstring(capital_city_response.content)
    namespace = {'m': 'http://www.oorsprong.org/websamples.countryinfo'}

    assert (root.find('.//m:CapitalCityResult', namespace).text == "Warsaw"), "Capital City verfication failed"
    yield