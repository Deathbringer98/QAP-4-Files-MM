# QAP-4-Files-MM
Matthew Menchinton QAP 4 Python Project
Date: 2023-07-25
Project: 1 –Python –Lists and Data Files


Project 1 – Insurance Premium Calculator
Description:
The One Stop Insurance Company needs a Python program to handle insurance policy information and premium calculations for its customers. The program reads default values from the "OSICDef.dat" data file, which contains important variables such as the next policy number, basic premium, discount for additional cars, cost of extra liability coverage, cost of glass coverage, cost for loaner car coverage, HST rate, and processing fee for monthly payments.

Program 1: Insurance Premium Calculator
How to Use:

Ensure that the "OSICDef.dat" file contains the correct default values for insurance calculations.
Run the program, and it will read the default values from the file.
The program will prompt the user to enter customer information, such as first name, last name, address, city, province (with validation), postal code, and phone number.
The user will then input the number of cars being insured and various options like extra liability coverage, glass coverage, and loaner car coverage.
The user will also indicate if they want to pay in full or monthly (with validation).
The program will calculate the insurance premium based on the input provided.
A receipt will be generated and displayed on the screen, showing all the policy details and the calculated insurance premium.
The program will save the policy information, including the next policy number, all input values, and the total insurance premium, to the "Policies.dat" file for future reference.
The invoice date will be set as the current date, and the next payment date will be the first day of the next month.
The program allows the user to enter as many policies as they need and continues until the user decides to exit the program.
When the user exits the program, the current values will be written back to the "OSICDef.dat" file.
Insurance Premium Calculation:

Basic rate for the first automobile: $869.00
Discount for each additional automobile: 25%
Extra liability coverage cost per car: $130.00
Glass coverage cost per car: $86.00
Loaner car coverage cost per car: $58.00
HST rate: 15%
Processing fee for monthly payments: $39.99
Note:
Please ensure to update the "OSICDef.dat" file with the appropriate default values for accurate insurance premium calculations.

Project 2 – Sales Graph using Matplotlib
Description:
The second Python program in this project allows the user to enter the total amount of sales for each month from January to December. The program uses Matplotlib to create a graph representing the total sales ($) against the months.

Program 2: Sales Graph using Matplotlib
How to Use:

Run the program.
The program will prompt the user to enter the total amount of sales for each month from January to December. Note that if it's not the end of the year, some monthly values may be zero.
The program will create a graph using Matplotlib, with the y-axis representing the total sales ($) and the x-axis representing the months of the year (e.g., ["Jan", "Feb", "Mar", ...]).
The graph will display appropriate titles and other options for better visualization.
Note:
The program requires Matplotlib to be installed on your system to create the sales graph. If you don't have it installed, you can install it using the following command:

Copy code
pip install matplotlib
Instructions:

Ensure you have the required data ready for the total sales of each month.
Run the program and enter the total sales for each month as prompted.
The program will generate a graph representing the sales against the months, providing visual insights into the sales performance throughout the year.
