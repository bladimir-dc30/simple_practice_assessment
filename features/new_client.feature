Feature: Create New Client - Simple Practice Assessment

#  Background:
#    Given I open the web browser
#    When  I open simple practice website
# NOTE: background only works on first scenario


  @smoke @regression
  Scenario Outline: Create new client on the simplepractice website
    Given I open the web browser
    When  I open simple practice website
    And   I type <email> on the email input
    And   I type <password> on the password input
    And   I click on the sign in button
    Then  I validate that the simple practice website is displayed correctly
    And   I click on the create button
    And   I click on the create client button
    And   I verify that the create client modal is displayed correctly
    And   I type <first_name> on the first name input
    And   I type <last_name> on the last name input
    And   I click on the continue button
    And   I click on the clients button
    And   I type <search_client> on the search input
    Then  I validate that the client is displayed correctly
    And   I quit driver

    Examples:
      | email                  | password    | first_name | last_name | search_client |
      | somab63683@lewenbo.com | GoodLuck777 | jose       | perez     | jose perez    |


  @smoke @regression
  Scenario Outline: Displayed error message into the webpage with no last name
    Given I open the web browser
    When  I open simple practice website
    And   I type <email> on the email input
    And   I type <password> on the password input
    And   I click on the sign in button
    Then  I validate that the simple practice website is displayed correctly
    And   I click on the create button
    And   I click on the create client button
    And   I verify that the create client modal is displayed correctly
    And   I type <first_name> on the first name input
    And   I click on the continue button
    Then  I validat that the last name error message is displayed correctly
    And   I quit driver

    Examples:
      | email                  | password    | first_name |
      | somab63683@lewenbo.com | GoodLuck777 | jordan     |

  @smoke @regression
  Scenario Outline: Displayed error message into the webpage with no first name
    Given I open the web browser
    When  I open simple practice website
    And   I type <email> on the email input
    And   I type <password> on the password input
    And   I click on the sign in button
    Then  I validate that the simple practice website is displayed correctly
    And   I click on the create button
    And   I click on the create client button
    And   I verify that the create client modal is displayed correctly
    And   I type <last_name> on the last name input
    And   I click on the continue button
    Then  I validat that the first name error message is displayed correctly
    And   I quit driver

    Examples:
      | email                  | password    | last_name |
      | somab63683@lewenbo.com | GoodLuck777 | smith     |


#  NOTE: USE DIFFERENT add_email FOR EVERY EXECUTION
  @smoke @regression @test
  Scenario Outline: Create new client on the simplepractice website with full credentials
    Given I open the web browser
    When  I open simple practice website
    And   I type <email> on the email input
    And   I type <password> on the password input
    And   I click on the sign in button
    Then  I validate that the simple practice website is displayed correctly
    And   I click on the create button
    And   I click on the create client button
    And   I verify that the create client modal is displayed correctly
    And   I type <first_name> on the first name input
    And   I type <last_name> on the last name input
    And   I type <nickname> on the nickname input
    And   I select <month> on the month input
    And   I select <day> on the day input
    And   I select <year> on the year input
    And   I type <add_email> on the add email input
    And   I type <add_phone> on the add phone input
    And   I click on the continue button
    And   I click on the clients button
    And   I type <search_client> on the search input
    Then  I validate that the client is displayed correctly
    And   I quit driver

    Examples:
      | email                  | password    | first_name | last_name | search_client | nickname | month   | day | year | add_email        | add_phone  |
      | somab63683@lewenbo.com | GoodLuck777 | jose       | perez     | jose perez    | poncho   | October | 15  | 2005 | wtgdwud@test.com | 0123456789 |