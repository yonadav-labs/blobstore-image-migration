import os

import pyodbc
import requests

from google.cloud import datastore

APP_ID = 'billionacts'

client = datastore.Client()

kind = 'NetworkMember'
column = 'LogoKey'

os.environ['APPLICATION_ID'] = APP_ID

query = client.query(kind=kind)
query_iter = query.fetch(limit=15)

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': 'CONSENT=YES+JP.en+20180603-18-0; SEARCH_SAMESITE=CgQI7I0B; OSID=pAfPEznfeJ-wo47TLKSZb0cTr0dLgvRQ0iK_CDUXmun4PecrnUvJXHYPcOQxPrwuAA_UnA.; _ga=GA1.3.1415783653.1570218135; _gcl_au=1.1.1818324880.1570261534; HSID=AkBlSajwmsVWx8Ge1; SSID=A_XCrV-f7kPtRZ3Ke; APISID=_2_SHjqAnk_mDpQr/AH0RhVEakBkCFW6S7; SAPISID=IsTcnWdGbA2Fy9ZZ/Am08rx2p3LfPqCbN9; SID=pAfPE9I_88fy9md9XFfitN8HAChXYrYGITPEoHNwdnsiQVtq1cgBLiVnV8r6tPCPbE_fag.; NID=188=HDdGvXds7S7dItWt6VjFdNumUs6OUZnvX7OnEUFF1bCZ4Bq2ZDr3AiHKLPrIkBFW88XNZd_l-xJyDk-rkjx1bUqosopXpoiNd45zbU0PF2VzG__fkbpknnihqW80yE3NiUZXry3nTiRjZXLTnw_IltRfZ3uJc6bmEJ5V9LNPTmJJcAGJfLJQINiuhXv7ajpwxqrD7rTvWgjFOcVz_qw8wvCHVn7wMkzaGV7U4x8tcLXgekavnTDtihPdn6iFWwIk6P6FHLRX6nhXem1CrPe1oymYuuexiOcQc00DR4J2-ixnqVKlI4t56B2YQ-PCeC_E75h6gvyD; ANID=AHWqTUko5aWRMSjjTLsaPxdvVAFh0I841T-2kdi_AYbZ-tnV4yl2WZf3QlqL2lWW; __utmc=243896023; 1P_JAR=2019-10-7-11; __utma=243896023.1415783653.1570218135.1570444997.1570447973.8; __utmb=243896023.0.10.1570447973; __utmz=243896023.1570447973.8.6.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); SIDCC=AN0-TYviA5-Y7SaS9m5Mbv4OYgIBQxA9tzKw_wmdPQr2dg_WCWXeLo3kJARHB1KMKkNDRHjh8Su1',
    'referer': 'https://console.cloud.google.com/appengine/blobstore/details?name=AMIfv974ROWsnpkYy7T-9GW9SRX07UCcHgMVmyHExcQyIibaADFp6FoL9hZ2N0CghcROlE-vzIRlX-UVBOsY4C8Ex2yTJ3JKhR9vfjMAVN5kpCqW25PS3Zc-dpv__v_fqGkMuhO_BBgZHo7HDZ6qD1qCq9Es31aLqA&project=billionacts',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'x-client-data': 'CJe2yQEIprbJAQjEtskBCKmdygEI4qjKAQjLrsoBCMqvygEIzrDKARjEscoB' 
}

for entity in query_iter:

    filename = '../images/{}/{}.png'.format(kind, entity['Name'])
    image_key = entity[column]

    url = "https://console.cloud.google.com/m/blobstore/download?pid=billionacts&blob=" + image_key

    res = requests.get(url, headers=headers)
    with open(filename, 'w') as f:
        f.write(res.content)

# cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
#                       "Server=oceanringtech.database.windows.net;"
#                       "Database=BillionActs;"
#                       "User ID=db_billionacts;Password=piecej@mf0und;"
#                       "Trusted_Connection=yes;")
# cursor = cnxn.cursor()

# main(cursor)

# cursor.close()
# cnxn.close()