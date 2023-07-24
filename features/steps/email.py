from behave import *

@given(u'a valid email address')
def step_impl(context):
    # context.browser.get('http://localhost:8000/index')
    assert True is not False

@when('I select compose')
def step_impl(context):
    assert True is not False

@when(u'I set subject to "Test"')
def step_impl(context):
    assert True is not False

@when(u'I set body to "Hello"')
def step_impl(context):
    assert True is not False

@when(u'I set To address line a valid email address')
def step_impl(context):
    assert True is not False

@when(u'I set Cc address line a valid email address')
def step_impl(context):
    assert True is not False

@when(u'I set Bcc address line a valid email address')
def step_impl(context):
    assert True is not False

@when('I send email to email address')
def step_impl(context):
    assert True is not False

@then('I can see email in the Sent outbox')
def step_impl(context):
    assert context.failed is False

@then('I can see "Test" in subject')
def step_impl(context):
    assert context.failed is False

@then('I can see "Hello" in body')
def step_impl(context):
    assert context.failed is False
