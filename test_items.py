import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_busket_button_is_visible(browser):
    browser.get(link)
    time.sleep(30)
    add_to_basket_button = browser.find_element(By.ID, "add_to_basket_form")
    assert add_to_basket_button.is_displayed(), "Кнопка не отображается"
