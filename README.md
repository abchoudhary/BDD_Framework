# BDD_Framework using Behave
**Behaviour driven development is an agile software development technique that encourages collaboration between developers, QA and non-technical business participants in a software project.**

**Behave operates on following directories:**
* __Feature Files__: written by Business analyst or sponser with behaviour scenarios in it.
  * Scenarios are written in this file using Gherkin Keywords.
  ```
  Example: feature_file.feature
  Feature: Name of the feature
    Scenario: Short description
      Given A pre-condition
      When  Some event
      Then  Some outcome
  ```
* __Steps__: directory with python implementation for the scenarios.
  * For every step in a scenario, we have to write step definition methods in the steps file.
  ```
  Example: feature_file_steps.py
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
 ** Used to pass multiple parameters.
 ** It will execute multiple times based on number of parameter provided. For Example:
 ```
 Feature:
  Scenario Outline:
   Given
   When
   And
   And
   Then
   Examples:
   | Username | Password |
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
**Command to run from terminal:**
```
 behave features\feature_file.feature   and press Enter
```
**Allure Reports:**
```
 pip install allure-behave
 To run from terminal: behave -f allure-behave.formatter:AllureFormatter -o Reports/  Features/
```
