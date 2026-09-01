\# My Submission



\*\*Name:\*\* Unman Chaudhuri

\*\*Enrollment Number:\*\* 12023052002212



\## Description



Hello everyone,

For Assignment 1, Web Element Identification, I am going to demonstrate how to locate different web elements on a webpage using Selenium WebDriver. The objective of this assignment is to understand and implement 5 different locator strategies: By.ID, By.NAME, By.TAG\_NAME, By.LINK\_TEXT, and By.CLASS\_NAME. For this demo, I am using Python Selenium with ChromeDriver, and the test site is the-internet.herokuapp.com/login, which is a standard practice site for Selenium. You can also use the local test\_page.html file I created. Here is how I implemented each locator as per the requirement: 

First, By.ID. I located the username field by its ID, which is 'username'. ID is the most preferred locator because it is unique.

Second, By.NAME. I located the password field by its Name attribute, which is 'password'.

Third, By.CLASS\_NAME. I located the login button using its class name 'radius'.

Fourth, By.TAG\_NAME. I located the page header using the tag name 'h2'. This is useful when we want to get all elements of a particular tag.

And fifth, By.LINK\_TEXT. I located the footer link using its exact visible text, 'Elemental Selenium'.

In the script, I have also used an explicit wait to make the test stable, and I will print a confirmation message for each locator that is found successfully. Now, I will run the script and you will see the browser open, locate all five elements, fill in the credentials, and print the success messages in the console. Let's execute.

