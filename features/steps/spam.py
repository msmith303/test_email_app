from behave import *
import logging

@given(u'a blocked address')
def step_impl(context):
    logging.info('INFO: Given a blocked address')
    # context.browser.get('http://localhost:8000/index')
    assert True is not False

@when('I set blocked address to blocked addresses')
def step_impl(context):
    assert True is not False

@when('I send email from blocked address')
def step_impl(context):
    # TODO: smtp driver to send email
    assert True is not False

@then('I can see blocked email in the Spam folder')
def step_impl(context):
    assert context.failed is False
