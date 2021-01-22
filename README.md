# BDD_Framework using Behave
**Behaviour driven development is an agile software development technique that encourages collaboration between developers, QA and non-technical business participants in a software project.**

**Behave operates on following directories:**
* Feature Files: written by Business analyst or sponser with behaviour scenarios in it.
  * Scenarios are written in this file using Gherkin Keywords.
  ```Example:
  Feature: Name of the feature
    Scenario: Short description
      Given A pre-condition
      When  Some event
      Then  Some outcome
  ```
* Steps: directory with python implementation for the scenarios.

