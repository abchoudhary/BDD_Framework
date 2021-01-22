# BDD_Framework using Behave
**Behaviour driven development is an agile software development technique that encourages collaboration between developers, QA and non-technical business participants in a software project.**

**Behave operates on following directories:**
* __Feature Files__: Written by Business analysts or sponsers with behaviour scenarios in it.
  * Scenarios are written in this file using Gherkin Keywords. For Example: feature_file.feature
  ```
  Feature: Name of the feature
    Scenario: Short description
      Given A pre-condition
      When  Some event
      Then  Some outcome
  ```
* __Steps__: Directory with python implementation for the scenarios.
  * For every step in a scenario, we have to write step definition methods in the steps file. For Example: feature_file_steps.py
  ```
  from behave import *
  from selenium import webdriver

  @given("A pre-condition)
  def step_impl(context):
    performing action using selenium like initializing webdriver object

  @when("Some event")
  def step_impl(context):
    performing action using selenium like entering url or performing other action

  @then("Some outcome")
  def step_impl(context):
    performing action using selenium like validating and asserting
  ```
__Project Structure__:
```
Project
  |
  Features(directory)
      |
      feature_file.feature
      Steps(directory)
           |
           feature_file_steps.py
```
**Scenario Outline:**
 * Used to pass multiple parameters.
 * It will execute multiple times based on number of parameter provided. For Example:
 ```
 Feature: Orange HRM Login
  Scenario Outline: Login to Orange HRM with multiple parameters
   Given Launch chrome browser
   When Open Orange HRM homepage
   And Enter username "<username>" and password "<password>"
   And Click on login button
   Then User must successfully login to the dashboard
   Examples:
   | username | password |
   | admin    | admin123 |
   | admin123 | admin    |
   | adminxyz | admin123 |
   | admin    | adminxyz |
```
**Background:**
To execute fixed number of steps before each scenario. For Example:
```
 Background: common steps
  Given Launch Browser
  When Open application
  And Enter username and password
  And Click login
```
**Tagging:**
 * You can tag your feature, or part of a feature like a scenario or example part of your scenario outline.
 * common use case is to tag the scenario you are working on to just test that one case.
 ```
  @wip
  Scenario: Short description
      Given A pre-condition
      When  Some event
      Then  Some outcome
 ```
 * To run feature with Tag:
 ```
  behave --tags=@wip                       (run feature which is tagged @wip)
  behave --tags="@wip or @slow"            (run feature which is tagged @wip or tagged @slow)
  behave --tags="@wip and @slow"           (run feature which is tagged both @wip and @slow)
  behave --tags=~@wip                      (run all features except @wip)
 ```
**Command to run from terminal:**
```
 behave features\feature_file.feature
```
**Allure Reports:**
```
 Installation: pip install allure-behave
 To run from terminal: behave -f allure-behave.formatter:AllureFormatter -o reports/  Features/
```
* json files will be generated in the reports folder. Run `allure serve reports_directory_path` command to generate and open report in your browser.

