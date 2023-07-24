Feature: Can I Identify Spam?
  All email addresses identified as spam by the user shall be automatically sent to the spam folder

  Scenario: Add an email address to blocked addresses
    Given a blocked address
    When I set blocked address to blocked addresses
    When I send email from blocked address
    Then I can see blocked email in the Spam folder
