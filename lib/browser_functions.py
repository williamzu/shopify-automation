import time
import traceback
from lib import functions as fc
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


if fc.system_is_windows():
    chrome_driver_location = fc.resources_project_path("chromedriver.exe")
else:
    chrome_driver_location = fc.resources_project_path("chromedriver")


# SHOPIFY
def shopify_login(shopify_url, email, password):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(chrome_driver_location, options=options)
    driver.set_window_position(0, 0)
    driver.set_window_size(1920, 1080)
    driver.get(shopify_url + "/admin/products?selectedView=all")
    # Login Information
    driver.find_element_by_id("account_email").clear()
    driver.find_element_by_id("account_email").send_keys(email, Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_id("account_email").send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_id("account_password").clear()
    driver.find_element_by_id("account_password").send_keys(password, Keys.ENTER)
    time.sleep(5)
    # Login Ends
    return driver


def shopify_make_product_available_to_all_channels(product_id, shopify_url, email, password):
    try:
        driver = shopify_login(shopify_url, email, password)
        driver.get(shopify_url + "/admin/products/" + str(product_id))
        driver.find_element_by_xpath("//button[contains(.,'Manage')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//button[contains(.,'Select all')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//button[contains(.,'Done')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//button[contains(.,'Save')]").click()
        driver.quit()
    except:
        traceback.print_exc()


def shopify_make_all_products_available_to_all_channels(shopify_url, email, password):
    try:
        driver = shopify_login(shopify_url, email, password)
        element = driver.find_element_by_id("PolarisCheckbox1")
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(element, 1, 1)
        action.click()
        action.perform()
        time.sleep(1)
        driver.find_element_by_xpath("//button[contains(.,'Select all 50+ products in your store')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[contains(.,'More actions')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[contains(.,'Add available channel(s)...')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[contains(.,'Make products available')]").click()
        print("All products available now")
        time.sleep(5)
        driver.quit()
    except:
        traceback.print_exc()
        pass


def shopify_make_all_collections_available_to_all_channels(shopify_url, email, password):
    try:
        driver = shopify_login(shopify_url, email, password)
        element = driver.find_element_by_id("PolarisCheckbox1")
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(element, 1, 1)
        action.click()
        action.perform()
        time.sleep(1)
        driver.find_element_by_xpath("//button[contains(.,'Select all 50+ collections in your store')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[contains(.,'More actions')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[contains(.,'Make collections available')]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[contains(.,'Make collections available')]").click()
        print("All collections available now")
        time.sleep(5)
        driver.quit()
    except:
        traceback.print_exc()
        pass


# Function to buy products using the Bogus Gateway as a payment method
def shopify_buy_products_automatically_bogus_test_mode(shopify_url, email, password, test_mode_password):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(chrome_driver_location, options=options)
    driver.set_window_position(0, 0)
    driver.set_window_size(1920, 1080)
    driver.get(shopify_url)
    driver.find_element_by_xpath('//a[@href="'+ "#LoginModal" +'"]').click()
    time.sleep(1)
    driver.find_element_by_id("Password").clear()
    driver.find_element_by_id("Password").send_keys(test_mode_password)
    driver.find_element_by_id("Password").send_keys(Keys.ENTER)

    # Login
    driver.get(shopify_url + "/account/login")
    driver.find_element_by_id("CustomerEmail").clear()
    driver.find_element_by_id("CustomerEmail").send_keys(email)
    driver.find_element_by_id("CustomerPassword").clear()
    driver.find_element_by_id("CustomerPassword").send_keys(password)
    driver.find_element_by_id("CustomerPassword").send_keys(Keys.ENTER)

    driver.get(shopify_url)

    for x in range(2):
        driver.find_elements_by_xpath("//button[contains(.,'Add to cart')]")[0].click()
        driver.find_elements_by_xpath("//button[contains(.,'Add to cart')]")[1].click()
        driver.find_elements_by_xpath("//button[contains(.,'Add to cart')]")[2].click()
        driver.find_elements_by_xpath("//button[contains(.,'Add to cart')]")[3].click()

    driver.get(shopify_url + "/cart")
    time.sleep(2)
    driver.find_element_by_name("checkout").click()
    time.sleep(2)
    driver.find_element_by_xpath("//button[contains(.,'Continue to shipping')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//button[contains(.,'Continue to payment')]").click()
    time.sleep(2)
    # driver.find_element_by_css_selector("form[name='number']").clear()
    # driver.find_element_by_id("for[name='number']").send_keys("1")
    # driver.find_element_by_xpath("//button[contains(.,'Pay now')]").click()
    time.sleep(1)
    driver.find_element_by_xpath("//form[contains(.,'Card number')]").click()
    actions = ActionChains(driver)
    actions.send_keys('Test')
    actions.perform()

    time.sleep(1)
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB)
    actions.perform()
    time.sleep(1)
    actions = ActionChains(driver)
    actions.send_keys('11')
    actions.perform()
    time.sleep(1)
    actions = ActionChains(driver)
    actions.send_keys('25')
    actions.perform()
    time.sleep(1)
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB)
    actions.perform()
    time.sleep(1)
    actions = ActionChains(driver)
    actions.send_keys('111')
    actions.perform()
    time.sleep(1)
    for y in range(14):
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.perform()
    time.sleep(1)
    actions = ActionChains(driver)
    actions.send_keys('1')
    actions.perform()
    time.sleep(1)
    driver.find_element_by_xpath("//button[contains(.,'Pay now')]").click()
    time.sleep(5)