Feature: Google Search BSC
  Scenario: Search for TestZeus
    Given I am on the Google homepage
    When I enter "BSC" in the search box
    And I click on the "Google Search" button
    Then I should see search results
    And Open the BSC Company URL