# reference: damienfrancois, CC BY-SA 4.0, 24 Nov 2013, https://stackoverflow.com/a/20180564
#Kenneth Reitz, Apache Software License (Apache 2.0), 5 Jan 2022, https://pypi.org/project/requests/

import requests
print(requests.__version__)
r = requests.get('http://google.com/')
print("google homepage status code", r.status_code)

