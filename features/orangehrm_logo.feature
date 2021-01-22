Feature: OrangeHRM Logo
  Scenario: Logo presence on OrangeHRM home page
    Given launch chrome browser
    When open orangeHRM homepage
    Then verify that the logo is present on the page
    And close browser