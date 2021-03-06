# Created by SanathKumar Vignesh at 22-06-2020
Feature: Login into Orange HRMS
  Testing the Login Screen

  Scenario Outline: Test the Login Screen
    Given I navigate to Orange Hrms website
    When I input the "<username>" and "<password>"
    And I click the login button
    Then I must navigate to the other page
    Examples:
    | username | password |
    | Admin    | admin123 |
    | admi     | admin123 |

    @test2
   Scenario: Login Screen Test
     Given I navigated to Orange HRMS website
     When I input <username> and <password>
       | username | password |
       | Admin | admin123 |
     And Click the Login button
     Then I navigate to dashboard