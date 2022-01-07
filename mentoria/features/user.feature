Feature: User

  Scenario: Add user (s5)
    Given a user with an administrator profile properly logged in version 1.9.12 of the platform #5 and on the Users page
    When the user clicks on Add User filling in the necessary data correctly
    Then the system returns a notification of the action s success And show the new user in the user list