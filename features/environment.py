import logging
import os

from features.browser import Browser
from features.pages.assignleave import LeavePage
from features.pages.home import HomePage
from features.pages.login import LoginPage


# from allure_behave.hooks import allure_report

def before_all(context):
    browser_obj = Browser()
    context.browser = browser_obj.get_driver()
    context.login = LoginPage(context.browser)
    context.home = HomePage(context.browser)
    context.assignleave = LeavePage(context.browser)
    context.log = logging
    print("Executing before all block")


# def before_feature(context, feature):
#      print("Before feature\n")

# Scenario level objects are popped off context when scenario exits
# def before_scenario():
#     pass


def after_scenario(context, scenario):
    print("scenario status" + str(scenario.status))
    if scenario.status == "failed":
        if not os.path.exists("failed_scenario_screenshots"):
            os.mkdir("failed_scenario_screenshots")
        os.chdir('failed_scenario_screenshots')
        context.browser.save_screenshot(str(scenario.name) + "_failed.png")


# def after_feature(context,feature):
#      print("\nAfter feature")
#
def after_all(context):
    print('Executing after all block')
    context.browser.quit()
    # allure_report("C:\\Users\\SanathKumar Vignesh\\PycharmProjects\\First_Project\\reports")
