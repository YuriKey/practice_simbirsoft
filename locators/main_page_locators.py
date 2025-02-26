from selenium.webdriver.common.by import By

name_field_locator = By.ID, 'name-input'
password_field_locator = By.XPATH, '//input[@type="password"]'
milk_checkbox_locator = By.CSS_SELECTOR, 'input[value="Milk"]'
coffee_checkbox_locator = By.ID, 'drink3'
yellow_radiobutton_locator = By.XPATH, '//*[@id="color3"]'
auto_type_menu_locator = By.CSS_SELECTOR, 'select[data-testid="automation"]'
auto_type_locator = By.XPATH, '//option[@data-testid="automation-yes"]'
email_field_locator = By.ID, 'email'
message_field_locator = By.XPATH, '//textarea[@id="message"]'
submit_button_locator = (By.XPATH, "//button[@class='custom_btn btn_hover']")
tools_area = By.XPATH, '//*[@id="feedbackForm"]/ul'




# modal_window_text_locator = By.XPATH, '//*[@id="modal"]'

