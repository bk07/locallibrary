import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_ll(self):
        user = "bk"
        pwd = "123"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://bk07.pythonanywhere.com/")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div[1]/ul/li[1]/a").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[1]/td[2]/input").send_keys(user)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input").send_keys(pwd)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div/div[2]/form/input[2]").click()
        time.sleep(3)
        time.sleep(1)
        driver.get("http://bk07.pythonanywhere.com/")
        # assert "Logged in"
        try:
            elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/h2")
            text = elem.text
            time.sleep(2)
            assert text == "Dynamic content"

        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False
        time.sleep(3)


def tearDown(self):
    self.driver.close()


if __name__ == "_main_":
    unittest.main()