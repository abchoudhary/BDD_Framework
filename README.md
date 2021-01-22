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
  * For every step in a scenario, we have to write step definition methods in the steps file.
* __Steps__: directory with python implementation for the scenarios.
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


