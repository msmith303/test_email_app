outside_email_test_app

This python module will test the Outside Analytics email application.  See the test procedure document for test cases, requirements, test approach and assumptions.

The test strategy is to use behavior driven development (BDD) which will involve stakeholders, test development and development.  Feature files will describe the end-to-end usage of this product and guide the test process.  Behavior-driven development (BDD) is an agile software development technique that encourages collaboration between developers, QA and non-technical or business participants in a software project.

Setup:
 1. mkdir pyenv_env/<my_shell_name)
 2. cd pyenv_env/<my_shell_name)
 3. pyenv virtualenv 3.8.16 <my_shell_name>
 4. pyenv shell <my_shell_name>
 5. pip install behave
 6. pip install selenium
 7. git clone msmith303/test_email_app

To run the tests:
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
 o Requirments Documentation [TBD] 
