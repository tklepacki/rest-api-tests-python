import requests

def get_capital_city(country_iso_code): 
    url = "http://oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
    headers = {
        "content-type": "text/xml"
    }
    body = f"""<?xml version="1.0" encoding="utf-8"?>
        <soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
        <soap12:Body>
            <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
            <sCountryISOCode>{country_iso_code}</sCountryISOCode>
            </CapitalCity>
        </soap12:Body>
        </soap12:Envelope>"""

    session = requests.session()
    response = session.post(url, data=body, headers=headers)

    return response
