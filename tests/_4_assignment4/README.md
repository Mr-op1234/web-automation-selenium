# My Submission

**Name:** Alokita Dutta
**Enrollment Number:** 12023052017058

## Description

This submission covers Assignment 4: Child Nodes Using CSS. The script uses Selenium
WebDriver with CSS child selectors to locate and interact with elements nested inside
a specific parent form on a login page.

Assignments 1-3 covered locating single elements (By.ID, By.NAME, etc.), locating
multiple elements of the same type, and using CSS selectors with wildcards for dynamic
attributes. Assignment 4 builds on this by scoping selectors to a parent element
(e.g. `#login input[name='username']` and `#login > button`), ensuring the correct
nested element is located even if similar tags exist elsewhere on the page.

The script automates logging into the practice site the-internet.herokuapp.com,
filling the username and password fields (both children of the `#login` form), and
clicking the login button (a direct child of the same form), then verifies success
by reading the confirmation message.

## Demo

[Add your video link here once uploaded — e.g. an unlisted YouTube link or Google Drive link]
