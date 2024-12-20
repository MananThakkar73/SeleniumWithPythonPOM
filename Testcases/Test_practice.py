import pytest

from Testcases import conftest
from Testcases.conftest import startup
from Utility.BaseClass import Baseclass
from selenium.webdriver.common.by import By
from Webpages.LoginPage import Loginpage
from Webpages.onepage import onepage

@pytest.mark.usefixtures("startup")
class TestPractice:

    @pytest.fixture(params=Baseclass.datafromexcel(conftest.home_dir+"\\PycharmProjects\\SeleniumWithPythonPOM\\TestData\\datapractice.xlsx", "Sheet1"))
    def getdata(self,request):
        return request.param

    @pytest.mark.Regression
    def test_001(self, getdata):
        Baseclass.element_present(self, onepage.get_emailid(self=onepage))
        #onepage.emailId_Present(self=onepage.)
        Baseclass.element_present(self,onepage.get_password(self= onepage))
        Baseclass.element_present(self,onepage.get_loginButton(self=onepage))
        onepage.test1_loginMethod(self,getdata[0],getdata[1])

    @pytest.mark.Regression
    def test_002(self):
        #Baseclass.move_to_elment(self,onepage.test2_values)
        onepage.test2_valuesinsection(self,3)
        onepage.test2_nameOfvalue(self, "List Item 2 6", 2)
        onepage.test2_valueofvalue(self, "6", 2)

    @pytest.mark.Regression
    def test_003(self):
        Baseclass.move_to_elment(self,onepage.test3_dropdown)
        onepage.test3_selectedDropdownname(self,"Option 1")
        Baseclass.dotclick(self,onepage.test3_dropdown)
        Baseclass.dotclick(self,onepage.test3_dropdown_click)
        onepage.test3_selectedDropdownname(self, "Option 3")


    def test_004(self):
        Baseclass.move_to_elment(self,onepage.test4_button1)
        Baseclass.button_enable(self,onepage.test4_button1)
        Baseclass.button_disable(self, onepage.test4_button2)


    def test_005(self):
        Baseclass.move_to_elment(self,onepage.test6_text)
        Baseclass.element_wait(self,onepage.test5_button1,10)
        Baseclass.dotclick(self,onepage.test5_button1)
        Baseclass.element_present(self,onepage.test5_alert)
        Baseclass.button_disable(self,onepage.test5_button1)

    def test_006(self):
        Baseclass.move_to_elment(self, onepage.test6_text)
        onepage.anyValuFromTable(self,2,2, "Ventosanzap")


