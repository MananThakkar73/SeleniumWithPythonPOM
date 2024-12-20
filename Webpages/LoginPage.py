from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Utility.BaseClass import Baseclass


class Loginpage(Baseclass):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    emai_id = (By.ID,"user-name")
    paswd = (By.ID,"password")
    login = (By.ID,"login-button")

    def loginin(self,email,pasd):
        self.driver.find_element(*Loginpage.emai_id).send_keys(email)
        self.driver.find_element(*Loginpage.paswd).send_keys(pasd)
        self.driver.find_element(*Loginpage.login).click()

