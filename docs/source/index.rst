.. pytonik curl documentation master file, created by
   sphinx-quickstart on Sun Feb 23 08:15:42 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Pytonik Curl
============

This document refers to version |release|


Pytonik curl module support sending or initiating actions within or outside. 
It enables access to API’s and return respond back to the application, in form of JSON, HTML, RAW data etc.

In this case the use of curl module is to ``POST``, ``GET``,  ``HEAD``, ``PUT`` information in internal or from external API’s URL
using attributes like ``status``, ``reason``,  and ``result``.  Whereby ``status`` handles response codes.

example **200**, **404**, **500**, etc. which the ``reason`` of this status could be OK, Not Found, Internal server Error, etc.

Get excepted information from ``result``

Getting Started
===============

**How to install**

.. code-block:: python

   pip install pytonik-curl=1.0

**Import Module**

.. code-block:: python
   
   from pytonik_curl.curl import curl 


**Callable**


.. code-block:: python
   
   cl = curl() 



**Curl Local Variable**

.. code-block:: python

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



GET
----

**GET** retrieves information from api’s server and returns response ``status`` , ``reason``, and  ``result``

.. code-block:: python

   url = "https://example.com"
   cl = curl()
   cl.set(cl.URL, url)
   cl.set(cl.GET, '/users/{username}'.format(username='testme'))
   cl.finish()
   print(cl.status, cl.reason, cl.result())



HEAD
----

**HEAD** check api’s and returns response  ``status`` and ``reason``

.. code-block:: python

   url = "https://example.com"
   cl = curl()
   cl.set(cl.URL, url)
   cl.set(cl.HEAD, '/users')
   cl.finish()
   print(cl.status, cl.reason)
   	


GET
----
	
**POST**  sent data/information to api using parameters or arguments
and returns response ``status`` , ``reason``, and  ``result``

.. code-block:: python

   url = "https://example.com"
   cl = curl()
   cl.set(cl.URL, url)
   cl.set(cl.CONTENTHEADER, 'application/x-www-form-urlencoded')
   cl.set(cl.ACCEPTHEADER, 'text/plain')
   cl.set(cl.POST, '/add/users')
   cl.set(cl.POSTFIELDS, {'username':'testme', 'password':'test' })
   cl.finish()
   print(cl.status, cl.reason, cl.result('utf-8'))



Contact
-------

**Name:**  Pytonik MVC

**Email:** dev@pytonik.com
