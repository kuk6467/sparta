import requests

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

gus = rjson['RealtimeCityAir']['row']

for gu in gus:
    gus_name = gu['MSRSTE_NM']
    gu_mise = gu['IDEX_MVL']
    if gu_mise > 50:
        print(gus_name, gu_mise)
