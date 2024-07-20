import os

from selenium import webdriver
import pytest
home_dir = os.path.expanduser("~")
print(home_dir)

@pytest.fixture(params=["chrome"],scope="class")
def startup(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.get(home_dir+"/PycharmProjects/pythonProject/TestData/QE-index.html")
    request.cls.driver = driver
    driver.maximize_window()

    yield
    driver.quit()
