# Pytonik curl 

[![Build Status](https://img.shields.io/pypi/v/pytonik-curl)](https://pypi.python.org/pypi/pytonik-curl)
[![Downloads](https://img.shields.io/pypi/dm/pytonik-curl)](https://pypi.python.org/pypi/pytonik-curl/)
[![Wheel](https://img.shields.io/pypi/wheel/pytonik-curl.svg)](https://pypi.python.org/pypi/pytonik-curl)
[![Python Version](https://img.shields.io/pypi/pyversions/pytonik)](https://pypi.python.org/pypi/pytonik-curl)
[![License](https://img.shields.io/pypi/l/pytonik-curl)](https://pypi.python.org/pypi/pytonik-curl)

Pytonik ``curl`` module support sending or initiating actions within or outside. 
It enables access to API’s and return respond back to the application, in form of JSON, HTML, RAW data etc.
In this case the use of curl module is to ```POST```, ```GET```,  ```HEAD```, ```PUT``` information in internal or from external API’s URL
using attributes like ```status```, ```reason```,  and ```result```.  Whereby ```status``` handles response codes
example **200**, **404**, **500**, etc. which the ``reason`` of this status could be OK, Not Found, Internal server Error, etc.
Get excepted information from ``result``

[![Made with python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://pypi.python.org/pypi/pytonik-curl)



## How to install

We recommend you to install pytonik package using Terminal or Command Line Window

```$ pip install pytonik-curl=1.0.0 ```

**Import Module**

``` from pytonik_curl.curl import curl ```


**Callable**


``` cl = curl() ```


**Curl Local Variable**

```
URL #accept url link
HTTPHEADER #httpheader  application/x-www-form-urlencoded etc.
CONTENTHEADER #accept text/plain, html/plain etc.
TIMEOUT #accept
POSTFIELDS #accept dictionary formate {name: example, next: testing}
POST #accept folder or url part / or /mypath
GET	#accept folder or url part / or /mypath
HEAD #accept folder or url part / or /mypath
PUT #accept folder or url part / or /mypath
PORT #accept url port 8080

```

**GET** retrieves information from api’s server and returns response ``status`` , ``reason``, and  ``result``

```
url = "https://example.com"
cl = curl()
cl.set(cl.URL, url)
cl.set(cl.GET, '/users/{username}'.format(username='testme'))
cl.finish()
print(cl.status, cl.reason, cl.result())

```


**HEAD** check api’s and returns response  ``status`` and ``reason``

```
url = "https://example.com"
cl = curl()
cl.set(cl.URL, url)
cl.set(cl.HEAD, '/users')
cl.finish()
print(cl.status, cl.reason)
	
```	
**POST**  sent data/information to api using parameters or arguments
and returns response ``status`` , ``reason``, and  ``result``

```
url = "https://example.com"
cl = curl()
cl.set(cl.URL, url)
cl.set(cl.CONTENTHEADER, 'application/x-www-form-urlencoded')
cl.set(cl.ACCEPTHEADER, 'text/plain')
cl.set(cl.POST, '/add/users')
cl.set(cl.POSTFIELDS, {'username':'testme', 'password':'test' })
cl.finish()
print(cl.status, cl.reason, cl.result('utf-8'))

```

## Contact

**Name:**  Pytonik MVC

**Email:** dev@pytonik.com
