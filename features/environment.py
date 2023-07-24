from behave import fixture, use_fixture, model
from selenium import webdriver

@fixture
def selenium_browser_chrome(context):
    context.browser = webdriver.Chrome()
    yield context.browser
    # cleanup
    context.browser.quit()

# def before_all(context):
    # use_fixture(selenium_browser_chrome, context)
    # called after after_all() hook is called

# def before_feature(context, feature):
    # model.init(environment='test')
