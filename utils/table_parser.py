from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def get_name_list(browser):
    wait = WebDriverWait(browser, 10)
    table = wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))
    rows = table.find_elements(By.TAG_NAME, "tr")[1:]

    column_index = 0
    column_data = []

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) > column_index:
            column_data.append(cells[column_index].text.strip())

    return column_data
