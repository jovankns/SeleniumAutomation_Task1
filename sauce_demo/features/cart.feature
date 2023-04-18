@web @Cart
Feature: Cart

    Background:
      Given Go to "https://www.saucedemo.com/"
      When I log in to the site


    @Cart-1
    Scenario: Cart - User can add 1 item and cart badge is updated correctly
      When I add random item from the list to the cart
      Then the cart badge is updated correctly

    @Cart-2
    Scenario: Cart - User can add 2 item and 2 correct items are present in the cart
      When I add random item from the list to the cart
      And I open item's details page
      And I add the item to the cart
      And I open the cart
      Then the correct items are present

    @Cart-3
    Scenario: Cart - User can add 2 item and remove 1 item from the cart and correct item is present
      When I add random item from the list to the cart
      And I open item's details page
      And I add the item to the cart
      And I open the cart
      And I remove the first item from the cart
      Then the correct items are present
