Feature: Create New Client - Simple Practice Assessment

#  Background:
#    Given I open the web browser
#    When  I open simple practice website
# NOTE: background only work on first scenario


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