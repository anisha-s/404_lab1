# reference: damienfrancois, CC BY-SA 4.0, 24 Nov 2013, https://stackoverflow.com/a/20180564
# Kenneth Reitz, Apache Software License (Apache 2.0), 5 Jan 2022, https://pypi.org/project/requests/
# Arjun Thakur, 02 May 2019, https://www.tutorialspoint.com/downloading-files-from-web-using-python

import requests
print(requests.__version__)
r = requests.get('http://google.com/')
print("google homepage status code", r.status_code)

r1 = requests.get('https://raw.githubusercontent.com/anisha-s/cmput_404_lab1/main/lab1.py')
open('cmput404_lab1.py', 'wb').write(r1.content)
print('Printing cmput404_lab1.py') 
print(r1.text)
