from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Loginpage:
    def __init__(self,driver):
        self.driver = driver

    emai_id = (By.ID,"user-name")
    paswd = (By.ID,"password")
    login = (By.ID,"login-button")

    def loginin(self,email,pasd):
        self.driver.find_element(*Loginpage.emai_id).send_keys(email)
        self.driver.find_element(*Loginpage.paswd).send_keys(pasd)
        self.driver.find_element(*Loginpage.login).click()

