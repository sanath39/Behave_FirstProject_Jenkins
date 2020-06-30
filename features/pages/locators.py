class Locators:
    # Login page objects
    txtbox_username_xpath = "//input[@id='txtUsername']"
    txtbox_password_xpath = "//input[@id='txtPassword']"
    btn_login_xpath = "//input[@id='btnLogin']"
    span_invalid_info_xpath = "//span[@id='spanMessage']"

    # Home page objects
    btn_welcome_xpath = "//a[@id='welcome']"
    btn_logout_xpath = "//a[contains(text(),'Logout')]"
    span_leave_xpath = "//*[@id='menu_leave_viewLeaveModule']"
    span_assign_leave_xpath = "//*[@id='menu_leave_assignLeave']"
    span_quick_assign_leave_xpath = "//*[@id='dashboard-quick-launch-panel-menu_holder']/table/tbody/tr/td[1]/div/a/span"

    # Leave list Objects

    # Leave page objects
    txt_emp_name_xpath = "//input[@id='assignleave_txtEmployee_empName']"
    ddl_leave_type_xpath = "//select[@id='assignleave_txtLeaveType']"
    date_pick_from_date_xpath = "//input[@id='assignleave_txtFromDate']"
    date_pick_to_date_xpath = "//input[@id='assignleave_txtToDate']"
    ddl_part_days_xpath = "//select[@id='assignleave_partialDays']"
    txt_area_comment_xpath = "//textarea[@id='assignleave_txtComment']"
    btn_assign_xpath = "/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/p/input"
    btn_confirm_ok_xpath = "//input[@id='confirmOkButton']"

