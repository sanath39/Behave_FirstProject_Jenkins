# Created by SanathKumar Vignesh at 23-06-2020
Feature: Assign leave to an employee
  Testing the Assign Leave Screen

  Scenario: Testing the Assign Leave Screen
    Given I login to the OrangeHRMS
    When I click on the "Leave"
    And I click on the "Assign Leave"
    Then I must navigate to the Assign Leave page

  Scenario: Testing the Quick Assign Leave Screen
    Given I login to the OrangeHRMS
    When I click on the "Quick Assign Leave"
    Then I must navigate to the Assign Leave page

  Scenario: Testing For Assigning Leave To Employee
    Given I login to the OrangeHRMS
    When I click on the "Quick Assign Leave"
    And I Filling all the required fields to assign leave
    Then I must navigate to the Assign Leave page

