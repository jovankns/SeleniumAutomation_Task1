@web @CompleteOrder
Feature: CompleteOrder

    @CompleteOrder-1
    Scenario: CompleteOrder - User can add and remove items from the cart and complete checkout
      Given Go to "https://www.saucedemo.com/"
      When I log in to the site
      And I add random item from the list to the cart
      And I open item's details page
      And I add the item to the cart
      And I open the cart
      And I remove the first item from the cart
      And I continue to the Checkout page
      And I complete the checkout form
      And I complete the order
      Then the order is completed successfully with the displayed message