from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element("id", "username").send_keys("tomsmith")
driver.find_element("id", "password").send_keys("SuperSecretPassword!")
driver.find_element("css selector", "button.radius").click()
assert "You logged into a secure area!" in driver.page_source
driver.quit()
