Feature: High contrast

  Scenario: Enable High Contrast (s4)
    Given a user with an administrator profile properly logged in version 1.9.12 of the platform #4
    When the user clicks the high contrast icon
    Then the system updates a platform interface with high contrast enabled