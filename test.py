import requests


url = 'https://www.fec.gov/files/bulk-downloads/2020/weball20.zip'
r = requests.get(url, allow_redirects=False)

open('test1.zip', 'wb').write(r.content)
