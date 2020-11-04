import requests

def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_nginx():
    "GET request to url returns a 502"
    url = 'http://192.168.10.100/'
    resp = requests.get(url)
    assert resp.status_code == 200

def test_nginx_html():
    "GET request to url returns a 502"
    url = 'http://192.168.10.100/'
    resp = requests.get(url)
    assert resp.headers['content-type'] == 'text/html'

def test_home():
    "GET request to url returns a 502"
    url = 'http://192.168.10.100/'
    resp = requests.get(url)
    assert resp.status_code == 200

def test_app():
    "GET request to url returns a 200"
    url = 'http://192.168.10.101/'
    resp = requests.get(url)
    assert resp.status_code == 200

def test_app1():
    "GET request to url returns a 200"
    url = 'http://192.168.10.102/'
    resp = requests.get(url)
    assert resp.status_code == 200

# url = 'https://w3schools.com/python/demopage.php'
# x = requests.get(url, proxies = { "https" : "https://1.1.0.1:80"})
# print(x.text)

def test_app1():
    "GET request to url returns a 200"
    url = 'http://192.168.10.100'
    resp = requests.get(url, proxies = { "http" : "http://192.168.10.100"})
    assert resp.text == 200
