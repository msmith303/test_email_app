Outside Analytics testing

This python module will test the Outside Analytics email application.  See the test procedure document for test cases, requirements, test approach and assumptions.

The test strategy is to use behavior driven development (BDD) which will involve stakeholders, test development and development.  Feature files will describe the end-to-end usage of this product and guide the test process.  Behavior-driven development (BDD) is an agile software development technique that encourages collaboration between developers, QA and non-technical or business participants in a software project.

Setup:
 1. mkdir pyenv_env/<my_shell_name)
 2. cd pyenv_env/<my_shell_name)
 3. pyenv virtualenv 3.8.16 <my_shell_name>
 4. pyenv shell <my_shell_name>
 5. pip install behave
 6. pip install selenium
 7. git clone https://github.com/msmith303/test_email_app

To run the tests using the behave cli command:
 # behave

Future work:
 1. Implement tables to feature files.
 2. Start browser at beginning of each feature (E2E testing)
 3. From DOM, use element ids to validate.
 4. Validate back-end resources.
 5. Add tags (smoke, functional, all)
 6. Validate failures in logs.

Related documents:
 o https://behave.readthedocs.io/en/latest/
 o Requirements Documentation link

= = = = = = = = = = = = = = = = = = = = = =
Feature: email.feature

Feature: Can I Send Email?
  Send emails using To, Cc and/or Bcc address lines

  Scenario: Send a test email using To address line
    Given a valid email address
    When I select compose
    When I set subject to "Test"
    When I set body to "Hello"
    When I set To address line a valid email address
    When I send email to email address
    Then I can see email in the Sent outbox
    Then I can see "Test" in subject
    Then I can see "Hello" in body

  Scenario: Send a test email using Cc address line
    Given a valid email address
    When I select compose
    When I set subject to "Test"
    When I set body to "Hello"
    When I set Cc address line a valid email address
    When I send email to email address
    Then I can see email in the Sent outbox
    Then I can see "Test" in subject
    Then I can see "Hello" in body

  Scenario: Send a test email using Bcc address line
    Given a valid email address
    When I select compose
    When I set subject to "Test"
    When I set body to "Hello"
    When I set Bcc address line a valid email address
    When I send email to email address
    Then I can see email in the Sent outbox
    Then I can see "Test" in subject
    Then I can see "Hello" in body
