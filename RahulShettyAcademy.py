import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class RahulShettyAcademy:
    URL = "https://www.rahulshettyacademy.com/AutomationPractice/"
    s = Service('.\\chromedriver.exe')
    countryName = "Arm"
    test_name = "Karen"

    def setUp(self):
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.get(self.URL)
        self.driver.maximize_window()

    def test_title(self):
        assert "Practice Page" in self.driver.title

    def test_radio_btn(self):
        self.driver.find_element(By.XPATH, '//input[@value="radio3"]').click()
        assert self.driver.find_element(By.XPATH, '//input[@value="radio3"]').is_selected()

    def test_suggesstion_country(self):
        country_field = self.driver.find_element(By.ID, "autocomplete")
        country_field.send_keys(self.countryName)
        self.driver.implicitly_wait(5);
        self.driver.find_element(By.ID, "ui-id-1").click()

    def test_dropdown_example(self):
        self.driver.find_element(By.ID, "dropdown-class-example").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, '//option[@value="option3"]').click()
        assert self.driver.find_element(By.XPATH, '//option[@value="option3"]').is_selected()

    def test_checkbox(self):
        self.driver.find_element(By.ID, "checkBoxOption1").click()
        assert self.driver.find_element(By.ID, "checkBoxOption1").is_selected()

    def test_open_window(self):
        self.driver.find_element(By.ID, "openwindow").click()
        parrent_handle = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        title_to_assert = "QA Click Academy | Selenium,Jmeter,SoapUI,Appium,Database testing,QA Training Academy"
        for handle in all_handles:
            if handle != parrent_handle:
                self.driver.switch_to.window(handle)
                self.driver.find_element(By.XPATH, '//div[@style="position: absolute;'
                                                   ' inset: 0px; box-shadow: rgba(0, 0, 0, 0)'
                                                   ' 0px 0px 0px inset;"]').click()
                self.driver.maximize_window()
                assert title_to_assert in self.driver.title
                self.driver.close()
                break
        self.driver.switch_to.window(parrent_handle)

    def test_switch_tab_example(self):
        self.driver.find_element(By.ID, "opentab").click()
        parrent_handle = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        title_to_assert = "Rahul Shetty Academy Blog – All things about Software testing"
        for handle in all_handles:
            if handle != parrent_handle:
                self.driver.switch_to.window(handle)
                self.driver.find_element(By.XPATH, '/html/body/div/header/div[3]/div/'
                                                   'div/div[2]/nav/div[2]/ul/li[8]/a').click()
                assert title_to_assert in self.driver.title
                self.driver.close()
                break
        self.driver.switch_to.window(parrent_handle)

    def test_switch_to_alert_example(self):
        self.driver.find_element(By.ID, "name").send_keys(self.test_name)
        self.driver.find_element(By.ID, "alertbtn").click()
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.ID, "name").send_keys(self.test_name)
        self.driver.find_element(By.ID, "confirmbtn").click()
        self.driver.switch_to.alert.dismiss()

    def test_element_displayed_example(self):
        self.driver.execute_script("window.scrollTo(0,200)")
        self.driver.find_element(By.ID, "hide-textbox").click()
        assert self.driver.find_element(By.XPATH, '//*[@style ="display: none;"]')
        self.driver.find_element(By.ID, "show-textbox").click()
        assert self.driver.find_element(By.XPATH, '//*[@style ="display: block;"]')


    def test_web_table_fixed_header(self):
        action = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/fieldset[2]/div[1]')
        self.driver.implicitly_wait(5)
        action.move_to_element(element).perform()
        self.driver.execute_script("arguments[0].scrollTop = 200", element)


    def test_mouse_hover(self):
        action = ActionChains(self.driver)
        mouse_hover = self.driver.find_element(By.ID, "mousehover")
        action.move_to_element(mouse_hover).perform()
        top = self.driver.find_element(By.XPATH,"/html/body/div[4]/div/fieldset/div/div/a[1]")
        action.move_to_element(top).click().perform()
        self.driver.implicitly_wait(5)
        action.move_to_element(mouse_hover).perform()
        reload = self.driver.find_element(By.XPATH,"/html/body/div[4]/div/fieldset/div/div/a[2]")
        action.move_to_element(reload).click().perform()


    def test_iframes(self):
        iframe = self.driver.find_element(By.ID,"courses-iframe")
        self.driver.switch_to.frame(iframe)
        all_access_plan = self.driver.find_element(By.XPATH, "/html/body/div/header/div[3]/div/div/div[2]/nav/div[2]/ul/li[3]/a")
        self.driver.implicitly_wait(3)
        all_access_plan.click()

    def tearDown(self):
        self.driver.close()


rahul = RahulShettyAcademy()
rahul.setUp()
rahul.test_title()
rahul.test_radio_btn()
rahul.test_suggesstion_country()
rahul.test_dropdown_example()
rahul.test_checkbox()
rahul.test_open_window()
rahul.test_switch_tab_example()
rahul.test_switch_to_alert_example()
rahul.test_element_displayed_example()
rahul.test_web_table_fixed_header()
rahul.test_mouse_hover()
rahul.test_iframes()
rahul.tearDown()
