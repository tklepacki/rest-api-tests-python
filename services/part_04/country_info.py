import requests

def get_full_country_info(country_iso_code):
    url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
    headers = {'content-type': 'text/xml'}
    body = f"""<?xml version="1.0" encoding="utf-8"?>
            <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body>
                    <FullCountryInfo xmlns="http://www.oorsprong.org/websamples.countryinfo">
                        <sCountryISOCode>{country_iso_code}</sCountryISOCode>
                    </FullCountryInfo>
                </soap:Body>
            </soap:Envelope>"""

    session = requests.session()
    response = session.post(url, data=body, headers=headers)

    return response

def get_capital_city(country_iso_code):
    url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
    headers = {'content-type': 'text/xml'}
    body = f"""<?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
            <soap:Body>
                <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
                    <sCountryISOCode>{country_iso_code}</sCountryISOCode>
                </CapitalCity>
            </soap:Body>
        </soap:Envelope>"""

    session = requests.session()
    response = session.post(url, data=body, headers=headers)
    
    return response