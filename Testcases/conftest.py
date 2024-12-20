import os

from selenium import webdriver
import pytest
home_dir = os.path.expanduser("~")
print(home_dir)

@pytest.fixture(params=["chrome"],scope="class")
def startup(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.get(home_dir+"\\PycharmProjects\\SeleniumWithPythonPOM\\TestData\\QE-index.html")
    #we are writing this request.class.driver so that when any class
    # use this fixture they can use the driver without error
    request.cls.driver = driver
    driver.maximize_window()

    yield
    driver.quit()
