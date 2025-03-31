class AddCustomerLocators:
    FIRST_NAME_FIELD = ("xpath", "//input[@ng-model='fName']")
    LAST_NAME_FIELD = ("xpath", "//input[@ng-model='lName']")
    POST_CODE_FIELD = ("xpath", "//input[@ng-model='postCd']")
    ADD_BUTTON = ("xpath", "//button[@type='submit']")
    CUSTOMERS_LIST_BUTTON = ("xpath", "//button[@ng-class='btnClass3']")
