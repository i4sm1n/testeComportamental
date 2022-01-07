Feature: Forum

  Scenario: Create a Forum discussion (s1)
    Given a user with an administrator profile properly logged in version 1.9.12 of the platform And monitoring a company on the Forum page
    When the user clicks at + to create a new discussion And duly fill in the required fields
    Then the system adds the new topic to the Forum listing And notifies you that the topic was created successfully

  Scenario: Delete Forum topic (s2)
    Given a user with an administrator profile properly logged in version 1.9.12 of the platform #2 And monitoring a company on the Forum page #2
    When the user clicks the Delete button of the desired topic And confirms the action
    Then the system deletes the topic from the Forum listing And shows a notification of Publication removed successfully

#  Scenario: Valid login (1a)
 #   Given a user is in the LEAD platform login page
   #   When the user inserts his valid credentials
    #Then LEAD platform redirects the user to the home page

#  Scenario: Invalid login (2a)
 #   Given a user is in the LEAD platform login page #2
  #  When the user inserts a invalid username and a valid password
   # Then LEAD platform returns that the username or password is invalid
