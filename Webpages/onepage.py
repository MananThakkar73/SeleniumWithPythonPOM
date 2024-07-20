from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class onepage:

    def __init__(self,driver):
        self.driver = driver


    test1_emailadd = (By.ID,"inputEmail")
    test1_password = (By.ID,"inputPassword")
    test1_loginbutton = (By.XPATH,"//button[text()='Sign in']")

    test2_values = (By.XPATH,"//li[@class='list-group-item justify-content-between']")
    test2_value_values = (By.XPATH,"//span[@class='badge badge-pill badge-primary']")

    test3_dropdown = (By.ID,"dropdownMenuButton")
    test3_dropdown_click = (By.XPATH,"//a[text()='Option 3']")

    test4_button1 = (By.XPATH,"//div[@id='test-4-div']//button[1]")
    test4_button2 = (By.XPATH,"//div[@id='test-4-div']//button[2]")

    test5_button1 = (By.XPATH,"//div[@id='test-5-div']//button")
    test5_alert = (By.XPATH,"//div[@class='alert alert-success']")

    test6_text = (By.XPATH,"//h1[text()='Test 6']")


    def test1_loginMethod(self,email,pasword):
        self.driver.find_element(*onepage.test1_emailadd).send_keys(email)
        self.driver.find_element(*onepage.test1_password).send_keys(pasword)
        self.driver.find_element(*onepage.test1_password).send_keys(Keys.ENTER)

    def test2_valuesinsection(self,n):
        assert len(self.driver.find_elements(*onepage.test2_values)) == n

    def test2_nameOfvalue(self, name,m):
        test2_all = self.driver.find_elements(*onepage.test2_values)
        test2_value = test2_all[m-1].text
        #print(test2_value)
        assert test2_value == name

    def test2_valueofvalue(self, val, o):
        test2_value_all = self.driver.find_elements(*onepage.test2_value_values)
        test2_value_val = test2_value_all[o-1].text
        #print(test2_value_val)
        assert test2_value_val == val

    def test3_selectedDropdownname(self, dropname):
        dropdownname = self.driver.find_element(*onepage.test3_dropdown).text
        assert dropdownname == dropname

    def anyValuFromTable(self, i, j, tabval):
        tabl_val = self.driver.find_element(By.XPATH,"//tbody/tr["+ str((i+1)) + "]/td[" +str((j+1))+"]").text
        assert tabl_val == tabval


