import urllib3
import os
import requests
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
session = 0

def clear():
    os.system("cls")

def getMB():
    cookies = {
        'afck-httpsetting-backendpool-tmobile-capi-t-mobile-nl-main-httpsCORS': 'XXXXXX',
        'afck-httpsetting-backendpool-tmobile-capi-t-mobile-nl-main-https': 'XXXXXX',
    }

    headers = {
        'Authorization': 'Bearer XXXXXX',
        'Content-Type': 'application/vnd.capi.tmobile.nl.roamingbundles.v3+json; charset=utf-8',
    }

    data = '{"Bundles": [{"BuyingCode": "A0DAY"}]}'

    response = requests.post(
        'https://capi.t-mobile.nl:443/XXXXXX/customer/XXXXXX/subscription/316XXXXXX/roamingbundles',
        headers=headers, cookies=cookies, data=data, verify=False)

def createSession():
    global session
    session = 1
    a_session = requests.Session()
    a_session.get('https://www.t-mobile.nl/my/verbruik-en-kosten#bundle-usage-overview')
    global cookies
    cookies = a_session.cookies
    global headers
    headers = a_session.headers
    print("[+] New Session Created")

def checkMB():
    data = {
        '__UniqueContentId': '/row1/column1/cell1/Consumer/htblocks/wc902_application_dotnet/default/my/verbruikstatus/BundleUsage',
        '__BindingPrefix': 'Row1.Column1.Cell1.BundleUsage',
        'Row1.Column1.Cell1.BundleUsage.Refresh': '1'
    }

    response = requests.post('https://www.t-mobile.nl:443/my/verbruik-en-kosten', headers=headers, cookies=cookies,
                             data=data, verify=False)
    soup = BeautifulSoup(response.text, 'lxml')

    if 'text-large text-confirm' in response.text:
        print("")
    else:
        print("[!] Connection Issue, values could not be read!")
        exit(0)

    body1 = soup.find_all("td")[16]
    x1 = body1.text
    y1 = [int(i) for i in x1.split() if i.isdigit()]
    dagtegoed = (str(y1).replace('[', '').replace(']', ''))
    print('Dagtegoed NL: ' + str(dagtegoed) + ' MB')
    body2 = soup.find_all("td")[12]
    x2 = body2.text
    y2 = [int(i) for i in x2.split() if i.isdigit()]
    global aanvulling
    aanvuller = (str(y2).replace('[', '').replace(']', ''))
    print('1 GB-aanvuller NL: ' + str(aanvuller) + ' MB')
    aanvulling = aanvuller

print("[+] Loading...")

def functie():
    while True:
        import time
        time.sleep(3)
        getMB()
        if session == 0:
            createSession()
            checkMB()
        else:
            checkMB()
        if int(aanvulling) <= 299:
            getMB()
            print('[+] Added 1GB')
            time.sleep(60)
            clear()
            checkMB()
        else:
            clear()
            checkMB()

# timer()
functie()
