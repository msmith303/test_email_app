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
