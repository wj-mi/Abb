# -*-coding:utf-8 -*-
# @autor: wangjuan
# @time: 2018-03-09:23:00

import unittest
from selenium import webdriver


class newTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_django(self):
        self.browser.get('http://127.0.0.1:8000')

        assert 'Django' in self.browser.title


if __name__ == '__main__':
    unittest.main()
