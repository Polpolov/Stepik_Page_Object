from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
import time
import math

class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        self.guest_can_add_product_to_basket()

    def guest_can_add_product_to_basket(self):
        add_button = self.browser.find_element_by_css_selector("body.default:nth-child(2) div.container-fluid.page:"
                                                               "nth-child(3) div.page_inner div.content:nth-child(3) "
                                                               "article.product_page div.row:nth-child(1) "
                                                               "div.col-sm-6.product_main:nth-child(2) form."
                                                               "add-to-basket:nth-child(6) > button.btn.btn-lg."
                                                               "btn-primary.btn-add-to-basket:nth-child(3)")
        add_button.click()


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    time.sleep(5)


