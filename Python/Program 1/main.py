# Program Author: Matthew Menchinton
# Date: 2023-07-25

import datetime

# Function to read values from the defaults file
def read_defaults(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return [float(val.strip()) for val in lines]

# Read values from the defaults file and store them in variables
defaults = read_defaults("OSICDef.dat")
next_policy_number = int(defaults[0])
basic_premium = defaults[1]
discount_additional_cars = defaults[2]
extra_liability_cost = defaults[3]
glass_coverage_cost = defaults[4]
loaner_car_cost = defaults[5]
hst_rate = defaults[6]
processing_fee = defaults[7]

# Function to get customer information and calculate premium
def calculate_insurance_premium():
    while True:
        # Get customer information
        first_name = input("Enter your first name: ").title()
        last_name = input("Enter your last name: ").title()
        address = input("Enter your address: ")
        city = input("Enter your city: ").title()
        provinces = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]
        province = input("Enter your province (e.g., NL, ON): ").upper()
        postal_code = input("Enter your postal code: ")
        phone_number = input("Enter your phone number: ")

        # Validate the province
        while province not in provinces:
            print("Invalid province. Please enter a valid province code.")
            province = input("Enter your province (e.g., NL, ON): ").upper()

        # Get policy details
        num_cars = int(input("Enter the number of cars being insured: "))
        extra_liability_option = input("Extra liability coverage? (Y/N): ").upper()
        glass_coverage_option = input("Glass coverage? (Y/N): ").upper()
        loaner_car_option = input("Loaner car coverage? (Y/N): ").upper()
        payment_method = input("Pay in full or monthly? (Full/Monthly): ").title()

        # Calculate total extra costs
        extra_costs = (extra_liability_cost if extra_liability_option == "Y" else 0) + \
                      (glass_coverage_cost if glass_coverage_option == "Y" else 0) + \
                      (loaner_car_cost if loaner_car_option == "Y" else 0)

        # Calculate total insurance premium
        total_cars = num_cars + (num_cars - 1) * discount_additional_cars
        total_insurance_premium = basic_premium * total_cars + extra_costs

        # Calculate HST and total cost
        hst_amount = total_insurance_premium * hst_rate
        total_cost = total_insurance_premium + hst_amount

        # Calculate monthly payment
        if payment_method == "Monthly":
            monthly_payment = (total_cost + processing_fee) / 8
        else:
            monthly_payment = 0  # For "Full" payment, no monthly payment is needed.

        # Get the current date
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")

        # Calculate the payment due date (first day of the next month)
        payment_due_date = (datetime.datetime.now() + datetime.timedelta(days=31)).replace(day=1).strftime("%Y-%m-%d")

        # Print receipt
        print("=" * 57)
        print(" " * 19 + "One Stop Insurance Company")
        print("\n" + " " * 22 + "RECEIPT")
        print("=" * 57)
        print(f"Date:            {current_date}")
        print(f"Policy Number:   {next_policy_number}")
        print(f"Policy Holder:   {first_name} {last_name}")
        print(f"Address:         {address}")
        print(f"                 {city} {province}  {postal_code}")
        print(f"Phone Number:    {phone_number}")
        print("=" * 57)
        print(f"Number of vehicles insured:            {num_cars}")
        print(f"Basic premium:                        {basic_premium:9,.2f}")
        print(f"Additional liability coverage: {'Yes':<5}    {extra_liability_cost:,.2f}")
        print(f"Optional glass coverage:       {'No' if glass_coverage_option == 'N' else 'Yes':<5}        {glass_coverage_cost:,.2f}")
        print(f"Optional rental vehicle:       {'No' if loaner_car_option == 'N' else 'Yes':<5}     {loaner_car_cost:,.2f}")
        print(" " * 35 + "__")
        print(f"Total extra costs:                    {extra_costs:9,.2f}")
        print(" " * 35 + "__")
        print(f"Total premium:                        {total_insurance_premium:9,.2f}")
        print(f"HST:                                          {hst_amount:,.2f}")
        print(" " * 35 + "__")
        print(f"Total cost:                           {total_cost:9,.2f}")
        print(" " * 35 + "=" * 9)
        print(f"Payment frequency:                {payment_method}")
        print(f"Payment due date:                 {payment_due_date}")
        print(f"Payment amount:                   ${monthly_payment:.2f}")
        print("=" * 57)

        # Save data to Policies.dat file
        with open("Policies.dat", "a") as policies_file:
            policies_file.write(f"{next_policy_number}, {current_date}, {first_name}, {last_name}, {address}, "
                                f"{city}, {province}, {postal_code}, {phone_number}, {num_cars}, "
                                f"{extra_liability_option}, {glass_coverage_option}, {loaner_car_option}, "
                                f"{payment_method}, {total_insurance_premium:,.2f}\n")

        print("Policy information processed and saved.")

        # Ask if the user wants to continue adding policies
        another_policy = input("Do you want to add another policy? (Y/N): ").upper()
        if another_policy != "Y":
            break

    return monthly_payment

# Example usage:
next_policy_number = 1944
basic_premium = 869.00
discount_additional_cars = 0.25
extra_liability_cost = 130.00
glass_coverage_cost = 86.00
loaner_car_cost = 58.00
hst_rate = 0.15
processing_fee = 39.99

monthly_payment = calculate_insurance_premium()

# Function to update the defaults file with the new policy number
def update_defaults_file(filename, next_policy_number):
    with open(filename, 'r+') as file:
        lines = file.readlines()
        lines[0] = f"{next_policy_number}\n"

        # Rewind the file pointer and write the updated lines
        file.seek(0)
        file.writelines(lines)
        file.truncate()

# Update the defaults file with the new policy number
next_policy_number += 1
update_defaults_file("OSICDef.dat", next_policy_number)
