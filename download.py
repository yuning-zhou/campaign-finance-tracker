import requests
import zipfile
import os


url = 'https://www.fec.gov/files/bulk-downloads/2018/weball18.zip'
r = requests.get(url, allow_redirects=True)

open('Candidate18.zip', 'wb').write(r.content)

with zipfile.ZipFile('Candidate18.zip', 'r') as zip_ref:
    zip_ref.extractall()

os.rename('weball18.txt', 'Candidate18.txt')
