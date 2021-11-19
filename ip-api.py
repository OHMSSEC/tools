import requests

"""The API base path is
http://ip-api.com/json/{query}

{query} can be a single IPv4/IPv6 address or a domain name. If you don't supply a query the current IP address will be used.
Parameters

Query parameters (such as custom fields and JSONP callback) are appended as GET request parameters, for example:
http://ip-api.com/json/?fields=61439
fields	response fields optional
lang	response language optional
callback	wrap inside (JSONP) optional

There is no API key required.
http://ip-api.com/json/{query}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query"""


def ip_api(addr):
    fields = {'{query}': addr}
    req = requests.get(url="http://ip-api.com/json/", params=fields, timeout=5)
    resp = req.json()
    for c, i in resp.items():
        print(f"{c.upper()} | {i}")
    print(f"\n\t {req.headers['Date']}")
