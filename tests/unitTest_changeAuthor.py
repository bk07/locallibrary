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
        driver.get("http://bk07.pythonanywhere.com/admin")
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div/form/div[1]/input").send_keys(user)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div/form/div[2]/input[1]").send_keys(pwd)
        time.sleep(1)
        #click login
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div/form/div[3]/input").click()
        time.sleep(1)
        #change
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[2]/a").click()
        time.sleep(1)
        #click author
        driver.find_element_by_xpath(
            "/html/body/div/div[3]/div/div[1]/div/div/div/form/div[2]/table/tbody/tr/th/a").click()
        time.sleep(1)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div/form/div/fieldset/div[2]/div/input").send_keys('Dengey')
        time.sleep(3)
        time.sleep(1)
        # click author
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[1]/div/form/div/div/input[1]").click()
        # assert "Logged in"
        try:
            elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/h1")
            text = elem.text
            time.sleep(2)
            assert text == "Select author to change"

        except NoSuchElementException:
            self.fail("Logout Failed - user may not exist")
            assert False
        time.sleep(3)


def tearDown(self):
    self.driver.close()


if _name_ == "_main_":
    unittest.main()