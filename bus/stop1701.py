from bs4 import BeautifulSoup
import requests


def next():
    time = ""
    url = requests.get('https://realtimetcatbus.availtec.com/InfoPoint/Stops/Stop/1701')
    if url.status_code == requests.codes.ok:
        soup = BeautifulSoup(url.text, 'html.parser')
        times = []
        for t in soup.find_all('div', {'class':'edt-cell'}):
            times.append(t.contents[0].strip())
        return times[-1]
    # else return None
