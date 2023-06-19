# Booking testing

This repository contains scripts that utilize the Page Object Model (POM) to test hotel reservation and verify the correct manage of the reservation from Admin panel in Google Chrome and Mozilla Firefox browsers. POM is a design pattern that enhances code maintainability and test efficiency by separating page elements and actions into reusable objects. By implementing POM, these scripts offer an organized approach to automated testing.

## Prerequisites

Before running the scripts, ensure that you have the following prerequisites installed:

-   Python 3
-   pip 22

## Steps to Run

Follow these steps to run the scripts:

1.  Clone the repository to your local directory.
2.  Open the local directory using your preferred code editor, such as Visual Studio Code (VSC).
3.  Install all the required dependencies by running the following command:  `pip install -r requirements.txt`.
4.  Execute the test file by running the command:  `pytest Tests/test_BookingPage.py -v -n 2 --html=./BookingReport.html`.
5. Execute the test file by running the command:  `pytest Tests/test_AdminDBoardPage.py -n 2 -v --html=./AdminPanelReport.html`.
6.  The test reports will be generated as  `BookingReport.html` and `AdminPanelReport.html` .

By following these steps, you will be able to clone the repository, set up the necessary dependencies, and run the test file using pytest. The tests will run in parallel, with two browsers open to execute each test case. The resulting test report will be saved as  `BookingReport.html` and `AdminPanelReport.html`.

Feel free to explore the repository, modify the scripts, and add more test cases according to your testing requirements.
