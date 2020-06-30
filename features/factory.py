def login_func(context):
    context.browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
    context.login.setUsername("Admin")
    context.login.setPassword("admin123")
    context.login.click_login()
