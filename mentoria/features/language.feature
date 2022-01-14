Feature: Language

  Scenario: Change platform language (s3)
    Given a user with an administrator profile properly logged in version 1.9.12 of the platform #3 and on the Profile page
    When the user changes the language saving the change
    Then the system translates the entire platform into the chosen language And it presents a notification of change caused successfully

  Scenario: Change platform language #2(s3.1)
    Given a user with an administrator profile properly logged in version 1.9.12 of the platform #3 and on the Profile page #2
    When the user changes the language saving the change #2
    Then the system translates the entire platform into the chosen language And it presents a notification of change caused successfully #2
