import requests

def test_nginx():
    "GET request to url returns a 200"
    url = 'http://192.168.10.100/'
    resp = requests.get(url)
    assert resp.status_code == 200

def test_nginx_html():
    "GET request to url returns a 502"
    url = 'http://192.168.10.100/'
    resp = requests.get(url)
    assert resp.headers['content-type'] == 'text/html'

def test_app1():
    "GET request to url returns a 200"
    url = 'http://192.168.10.101/'
    resp = requests.get(url)
    assert resp.status_code == 200

def test_app2():
    "GET request to url returns a 200"
    url = 'http://192.168.10.102/'
    resp = requests.get(url)
    assert resp.status_code == 200
