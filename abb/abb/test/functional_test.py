# -*-coding:utf-8 -*-
# @autor: wangjuan
# @time: 2018-03-09:23:00


from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000')

assert 'Django' in browser.title
