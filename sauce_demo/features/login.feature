@web @Login
Feature: Login

    Background:
        Given Go to "https://www.saucedemo.com/"

    @Login-1
    Scenario: Login - Verify email field cannot be blank to login
        When the user not enter an email address
        And the user enter a password
        And the user clicks the Login button
        Then the error says, "Epic sadface: Username is required"

    @Login-2
    Scenario: Login - Verify Password field cannot be blank to login
        When the user not enter a password
        And the user enter an email address
        And the user click the Login button
        Then the error says, "Epic sadface: Password is required"

    @Login-3
    Scenario: Login - Verify that entering the correct Email and Password successfully logs in the User
        When the user enter a valid email address
        And the user enter a valid password
        And the user click the Login button
        Then the Inventory Page displays

    @Login-4
    Scenario: Login - Verify that an error displays if the Email entered does not match any existing User
        When the user enter the email address, "not_valid_user@saucedemo.com"
        And the user enter a valid password
        And the user click the Login button
        Then the error says, "Epic sadface: Username and password do not match any user in this service"

    @Login-5
    Scenario: Login - Verify than an error displays if the Password entered does not match the Password associated with the User Account
        When the user enter a valid email address
        And the user enter the wrong password
        And the user click the Login button
        Then the error says, "Epic sadface: Username and password do not match any user in this service"