# -*-coding:utf-8 -*-
# @autor: wangjuan
# @time: 2018-03-09:23:00

import unittest
import requests
from selenium import webdriver


DOMAIN = 'http://127.0.0.1:8000'


class newTest(unittest.TestCase):
    def test_index(self):
        url = DOMAIN + '/abb/index'
        res = requests.get(url)
        assert res.status_code == 200
        print(res.content)
        assert 'hello' in str(res.content)


if __name__ == '__main__':
    unittest.main()
