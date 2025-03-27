Feature: Login SimplePractice Webpage

  @smoke @regression
  Scenario Outline: Login into the webpage with valid credentials
    Given I open the web browser
    When  I open simple practice website
    And   I type <email> on the email input
    And   I type <password> on the password input
    And   I click on the sign in button
    Then  I validate that the simple practice website is displayed correctly

    Examples:
      | email                  | password    |
      | somab63683@lewenbo.com | GoodLuck777 |

  @regression
  Scenario Outline: Login error message into the webpage with invalid email
    Given I open the web browser
    When  I open simple practice website
    And   I type <email> on the email input
    And   I type <password> on the password input
    And   I click on the sign in button
    Then  I validate that the simple practice website is not displayed

    Examples:
      | email         | password    |
      | test@mail.com | GoodLuck777 |

  @regression
  Scenario Outline: Login error message into the webpage with invalid password
    Given I open the web browser
    When  I open simple practice website
    And   I type <email> on the email input
    And   I type <password> on the password input
    And   I click on the sign in button
    Then  I validate that the simple practice website is not displayed

    Examples:
      | email                  | password    |
      | somab63683@lewenbo.com | password123 |

  @regression @test
  Scenario: Login error required message into the webpage with no credentials
    Given I open the web browser
    When  I open simple practice website
    And   I click on the sign in button
    Then  I validate that the required error messages are displyed
