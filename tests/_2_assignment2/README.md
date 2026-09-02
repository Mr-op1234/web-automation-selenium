# Assignment 2: Multiple Element Identification

**Name:** Pankaj Gop
**Enrollment Number:** 12023052017064
**Class Roll Number:** 64
**Stream:** CSE(IOTCSBT)
**Group Number:** 52
**Institute:** IEM, Salt Lake

## Description

This submission contains the Python Selenium script for Assignment 2. The objective is to dynamically identify and interact with multiple web elements of the same type simultaneously.

Instead of hardcoding individual locators, this script utilizes Selenium's `find_elements` method to generate iteratable lists of WebElements.

## Technical Implementation (How it Works)

This script demonstrates working with multiple elements in two distinct ways:

1. **Interactive Batch Processing:**
   - **Logic:** The script locates all checkboxes on the page using `driver.find_elements(By.XPATH, "//input[@type='checkbox']")`.
   - **Execution:** It uses a Python `for` loop to iterate through the resulting list, clicking each checkbox. An inline `assert` statement verifies that every individual element's state changes to `selected`.
2. **Data Extraction:**
   - **Logic:** The script captures all anchor tags using `driver.find_elements(By.TAG_NAME, "a")`.
   - **Execution:** It filters the list for visible text and successfully extracts the display text, proving the ability to harvest data from grouped DOM elements.

## Demo Video

https://drive.google.com/drive/folders/1eViiQb6ikS4OxnT5ld2lxlMdKGTBK05X?usp=sharing
