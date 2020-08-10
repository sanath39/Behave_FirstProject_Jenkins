from behave import *

use_step_matcher("re")


@given("I navigate to Orange Hrms website")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")


@when('I input the "(?P<username>.+)" and "(?P<password>.+)"')
def step_impl(context, username, password):
    """
    :type context: behave.runner.Context
    :type username: str
    :type password: str
    """
    context.login.setUsername(username)
    context.login.setPassword(password)


@step("I click the login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.login.click_login()


@then("I must navigate to the other page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.browser.current_url == "https://opensource-demo.orangehrmlive.com/index.php/dashboard"


@given(u'I navigated to Orange HRMS website')
def step_impl(context):
    context.browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")


@when(u'I input <username> and <password>')
def step_impl(context):
    for each in context.table:
        context.login.setUsername(each['username'])
        context.login.setPassword(each['password'])
    context.log.info('Username and password set')


@when(u'Click the Login button')
def step_impl(context):
    context.login.click_login()
    context.log.info('Login Button Clicked')


@then(u'I navigate to dashboard')
def step_impl(context):
    context.login.setUsername('Sanath')
