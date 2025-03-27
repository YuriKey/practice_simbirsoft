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


def get_name_row(browser, name):
    wait = WebDriverWait(browser, 10)
    table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table.table")))

    header_row = table.find_element(By.TAG_NAME, "thead").find_element(By.TAG_NAME, "tr")
    headers = header_row.find_elements(By.TAG_NAME, "td")
    header_names = [header.text.strip().lower() for header in headers]

    if "first name" not in header_names:
        raise ValueError("The 'First Name' column not found.")

    first_name_index = header_names.index("first name")

    rows = table.find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr")

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) > first_name_index:
            row_data = {header_names[i]: cells[i].text.strip() for i in range(len(header_names))}
            if row_data.get("first name") == name.lower():
                return row_data

    return None
