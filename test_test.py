from __future__ import unicode_literals

from selenium import webdriver

client = webdriver.Firefox()

client.get('http://0.0.0.0:8000')