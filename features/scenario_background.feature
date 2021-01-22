Feature: OrangeHRM Login

  Background: common steps
    Given launch browser
    When open application
    And Enter valid username and password
    And click on login

  Scenario: Login to HRM application
    Then User must login to Dashboard page

  Scenario: Search user
    When navigate to search page
    Then search page should display

  Scenario: Advanced search user
    When navigate to advanced search page
    Then advanced search page should display