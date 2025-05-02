#!/usr/bin/env python
# coding: utf-8

# In[8]:


import csv

# Function to load the CSV file and store its content in a list
def load_csv_file():
    csv_list = []  # Initialize an empty list to store the CSV data
    while True:
        # Prompt user to enter the file name or quit the program
        file_name = input("Enter the CSV file name or enter 'q' to quit the program: ")
        
        if file_name.lower() == 'q':  # If user inputs 'q', exit the function
            print("Exiting the program.")
            return None
        
        try:
            # Try to open the CSV file with UTF-8 encoding
            with open(file_name, 'r', encoding='UTF-8') as csv_file:
                csv_list.clear()  # Clear any existing data in the list
                for line in csv_file:
                    # Split each line by commas and add it to the list
                    csv_list.append(line.strip().split(','))
            print("CSV file loaded successfully.")
            return csv_list  # Return the populated CSV list
        except FileNotFoundError as e:
            # If file is not found, print an error message
            print(f"File does not exist: {e}")

# ------------------------------
# Task A1: Filter and display data based on card category
# ------------------------------
def filter_by_card_category(csv_list):
    print("\nRetrieve client number, gender, education level, and income based on card category.")
    card_options = {'1': 'BLUE', '2': 'PLATINUM', '3': 'GOLD', '4': 'SILVER'}

    while True:
        print("\nSelect a Card Category:")
        for key, value in card_options.items():
            print(f"{key}. {value.capitalize()}")
        print("0. Quit to Main Menu")  # Changed from 'q' to '0'

        user_input = input("Enter your choice (1-4) or '0': ").strip()

        if user_input == '0':
            return 'quit'
        if user_input not in card_options:
            print("Invalid option. Try again.")
            continue

        selected_category = card_options[user_input]
        card_category = []

        for row in csv_list[1:]:
            if row[15].upper() == selected_category:
                card_category.append([row[0], row[2], row[4], row[13]])

        if card_category:
            print(f"\n{'Client_Num':<12} {'Gender':<8} {'Education_Level':<15} {'Income':<10}")
            print("_" * 45)
            for item in card_category:
                print(f"{item[0]:<12} {item[1]:<8} {item[2]:<15} {item[3]:<10}")
        else:
            print(f"No data found for the category '{selected_category}'.")

        again = input("\nTry another card category? (Yes/No): ").strip().lower()
        if again != 'yes':
            return

# ------------------------------
# Task A2: Filter and display data based on state
# ------------------------------
def filter_by_state(csv_list):
    print("\nRetrieve the age, gender, income, and credit card category of customers based on state of residence.")

    while True:
        print("\nType the State abbreviation (e.g., NY, TX, CA) or '0' to quit to Main Menu.")  # Changed from 'q' to '0'
        user_input = input("Enter state abbreviation: ").strip().upper()

        if user_input == '0':
            return 'quit'

        state_data = []

        for row in csv_list[1:]:
            if row[6].upper() == user_input:
                state_data.append([row[1], row[2], row[13], row[15]])

        if state_data:
            print(f"\n{'Customer_Age':<15} {'Gender':<8} {'Income':<10} {'Card_Category':<15}")
            print("-" * 50)
            for item in state_data:
                print(f"{item[0]:<15} {item[1]:<8} {item[2]:<10} {item[3]:<15}")
        else:
            print(f"No data found for state '{user_input}'.")

        again = input("\nTry another state? (Yes/No): ").strip().lower()
        if again != 'yes':
            return

# ------------------------------
# Task A3: Filter by marital status and number of dependents
# ------------------------------
def filter_by_marital_and_dependents(csv_list):
    print("\nRetrieve age, gender, education level, and job of customers based on marital status and dependents.")

    while True:
        marital_options = {'1': 'Single', '2': 'Married', '3': 'Unknown'}
        print("\nSelect Marital Status:")
        for key, value in marital_options.items():
            print(f"{key}. {value}")
        print("0. Quit to Main Menu")  # Changed from 'q' to '0'

        user_input = input("Enter your choice (1-3) or '0': ").strip()

        if user_input == '0':
            return 'quit'
        if user_input not in marital_options:
            print("Invalid option. Try again.")
            continue

        selected_marital = marital_options[user_input]
        marital_status = []

        for row in csv_list[1:]:
            if row[5].lower() == selected_marital.lower() and int(row[3]) > 3:
                marital_status.append([row[1], row[2], row[4], row[12]])

        if marital_status:
            print(f"\n{'Age':<15} {'Gender':<10} {'Education Level':<15} {'Customer Job':<10}")
            print("_" * 55)
            for item in marital_status:
                print(f"{item[0]:<15} {item[1]:<10} {item[2]:<15} {item[3]:<10}")
        else:
            print(f"No data found for marital status '{selected_marital}' with more than 3 dependents.")

        again = input("\nTry another marital status? (Yes/No): ").strip().lower()
        if again != 'yes':
            return
            
# ------------------------------
# Task A4: Filter based on loan status and age above 25
# ------------------------------
def filter_by_loan_and_age(csv_list):
    print("\nRetrieve the job, income, car ownership, and gender of customers older than 25 based on loan status.")

    while True:
        loan_options = {'1': 'yes', '2': 'no'}
        print("\nSelect Loan Status:")
        for key, value in loan_options.items():
            print(f"{key}. {value.capitalize()}")
        print("0. Quit to Main Menu")  # Changed from 'q' to '0'

        user_input = input("Enter your choice (1-2) or '0': ").strip()

        if user_input == '0':
            return 'quit'
        if user_input not in loan_options:
            print("Invalid option. Try again.")
            continue

        selected_loan = loan_options[user_input]
        loan_and_gender = []

        for row in csv_list[1:]:
            if row[10].lower() == selected_loan and int(row[1]) > 25:
                loan_and_gender.append([row[12], row[13], row[8], row[2]])

        if loan_and_gender:
            print(f"\n{'Customer_Job':<15} {'Income':<10} {'Car_Owner':<8} {'Gender':<10}")
            print("-" * 45)
            for item in loan_and_gender:
                print(f"{item[0]:<15} {item[1]:<10} {item[2]:<8} {item[3]:<10}")
        else:
            print(f"No data found for loan status '{selected_loan}' and age > 25.")

        again = input("\nTry another loan status? (Yes/No): ").strip().lower()
        if again != 'yes':
            return

# -----------------------------
# Main Menu Function 
# -----------------------------

def main():
    csv_list = None
    while True:
        if csv_list is None:
            csv_list = load_csv_file()  # Load CSV file if not already loaded
            if csv_list is None:  # If loading fails, break the loop
                break

        # Display menu options for the user to filter data
        print("\nSelect an option to filter data:")
        print("1. Filter by Card Category")
        print("2. Filter by State")
        print("3. Filter by Marital Status and Dependents")
        print("4. Filter by Loan Status and Age")
        print("0. Quit Program")

        choice = input("Enter your choice (1-4) or '0': ").strip()

        if choice == '1':
            result = filter_by_card_category(csv_list)  # Call function to filter by card category
        elif choice == '2':
            result = filter_by_state(csv_list)  # Call function to filter by state
        elif choice == '3':
            result = filter_by_marital_and_dependents(csv_list)  # Call function to filter by marital status and dependents
        elif choice == '4':
            result = filter_by_loan_and_age(csv_list)  # Call function to filter by loan status and age
        elif choice == '0':
            print("\nThank you for using our customer data explorer. Goodbye!")
            break  # Exit the program
        else:
            print("Invalid choice. Please try again.")
            continue

        if result == 'quit':  # If user selects to quit, return to main menu
            print("Returning to main menu.\n")
# -----------------------------
# Run the main function
# -----------------------------

if __name__ == "__main__":
    main()


# In[ ]:





# In[11]:


# ------------------------------
# Task c1: Filter and display data based on card category
# ------------------------------
def filter_by_card_category(csv_list):
    print("\nRetrieve client number, gender, education level, and income based on card category.")
    card_options = {'1': 'BLUE', '2': 'PLATINUM', '3': 'GOLD', '4': 'SILVER'}  # Dictionary of card options

    while True:
        # Display card category options
        print("\nSelect a Card Category:")
        for key, value in card_options.items():
            print(f"{key}. {value.capitalize()}")
        print("0. Quit to Main Menu")

        # Get user input
        user_input = input("Enter your choice (1-4) or '0': ").strip()

        if user_input == '0':  # Return to main menu
            return 'quit'
        if user_input not in card_options:
            print("Invalid option. Try again.")
            continue

        # Filter CSV data based on selected card category
        selected_category = card_options[user_input]
        card_category = []

        for row in csv_list[1:]:  # Skip header row
            if row[15].upper() == selected_category:
                card_category.append([row[0], row[2], row[4], row[13]])

        # Display filtered results
        if card_category:
            print(f"\n{'Client_Num':<12} {'Gender':<8} {'Education_Level':<15} {'Income':<10}")
            print("_" * 45)
            for item in card_category:
                print(f"{item[0]:<12} {item[1]:<8} {item[2]:<15} {item[3]:<10}")
        else:
            print(f"No data found for the category '{selected_category}'.")

        # Ask user if they want to try again
        again = input("\nTry another card category? (Yes/No): ").strip().lower()
        if again != 'yes':
            return

# ------------------------------
# Task c2: Filter and display data based on state
# ------------------------------
def filter_by_state(csv_list):
    print("\nRetrieve the age, gender, income, and credit card category of customers based on state of residence.")

    while True:
        # Prompt for state abbreviation
        print("\nType the State abbreviation (e.g., NY, TX, CA) or '0' to quit to Main Menu.")
        user_input = input("Enter state abbreviation: ").strip().upper()

        if user_input == '0':
            return 'quit'

        state_data = []

        # Filter based on state input
        for row in csv_list[1:]:
            if row[6].upper() == user_input:
                state_data.append([row[1], row[2], row[13], row[15]])

        # Display filtered results
        if state_data:
            print(f"\n{'Customer_Age':<15} {'Gender':<8} {'Income':<10} {'Card_Category':<15}")
            print("-" * 50)
            for item in state_data:
                print(f"{item[0]:<15} {item[1]:<8} {item[2]:<10} {item[3]:<15}")
        else:
            print(f"No data found for state '{user_input}'.")

        # Ask if user wants to continue
        again = input("\nTry another state? (Yes/No): ").strip().lower()
        if again != 'yes':
            return

# ------------------------------
# Task c3: Filter by marital status and number of dependents
# ------------------------------
def filter_by_marital_and_dependents(csv_list):
    print("\nRetrieve age, gender, education level, and job of customers based on marital status and dependents.")

    while True:
        # Marital status options
        marital_options = {'1': 'Single', '2': 'Married', '3': 'Unknown'}
        print("\nSelect Marital Status:")
        for key, value in marital_options.items():
            print(f"{key}. {value}")
        print("0. Quit to Main Menu")

        # User input
        user_input = input("Enter your choice (1-3) or '0': ").strip()

        if user_input == '0':
            return 'quit'
        if user_input not in marital_options:
            print("Invalid option. Try again.")
            continue

        selected_marital = marital_options[user_input]
        marital_status = []

        # Filter based on marital status and dependents > 3
        for row in csv_list[1:]:
            if row[5].lower() == selected_marital.lower() and int(row[3]) > 3:
                marital_status.append([row[1], row[2], row[4], row[12]])

        # Display results
        if marital_status:
            print(f"\n{'Age':<15} {'Gender':<10} {'Education Level':<15} {'Customer Job':<10}")
            print("_" * 55)
            for item in marital_status:
                print(f"{item[0]:<15} {item[1]:<10} {item[2]:<15} {item[3]:<10}")
        else:
            print(f"No data found for marital status '{selected_marital}' with more than 3 dependents.")

        # Ask to retry
        again = input("\nTry another marital status? (Yes/No): ").strip().lower()
        if again != 'yes':
            return
            
# ------------------------------
# Task c4: Filter based on loan status and age above 25
# ------------------------------
def filter_by_loan_and_age(csv_list):
    print("\nRetrieve the job, income, car ownership, and gender of customers older than 25 based on loan status.")

    while True:
        # Loan status options
        loan_options = {'1': 'yes', '2': 'no'}
        print("\nSelect Loan Status:")
        for key, value in loan_options.items():
            print(f"{key}. {value.capitalize()}")
        print("0. Quit to Main Menu")

        # User input
        user_input = input("Enter your choice (1-2) or '0': ").strip()

        if user_input == '0':
            return 'quit'
        if user_input not in loan_options:
            print("Invalid option. Try again.")
            continue

        selected_loan = loan_options[user_input]
        loan_and_gender = []

        # Filter by loan status and age > 25
        for row in csv_list[1:]:
            if row[10].lower() == selected_loan and int(row[1]) > 25:
                loan_and_gender.append([row[12], row[13], row[8], row[2]])

        # Display filtered data
        if loan_and_gender:
            print(f"\n{'Customer_Job':<15} {'Income':<10} {'Car_Owner':<8} {'Gender':<10}")
            print("-" * 45)
            for item in loan_and_gender:
                print(f"{item[0]:<15} {item[1]:<10} {item[2]:<8} {item[3]:<10}")
        else:
            print(f"No data found for loan status '{selected_loan}' and age > 25.")

        # Ask to retry
        again = input("\nTry another loan status? (Yes/No): ").strip().lower()
        if again != 'yes':
            return

# ------------------------------
# Main function to run the program
# ------------------------------
def main():
    csv_list = None  # Initialize CSV list
    while True:
        if csv_list is None:
            csv_list = load_csv_file()  # Load CSV file if not already loaded
            if csv_list is None:
                break  # Exit if file loading was not successful

        # Display main menu
        print("\n=== Credit Card Analysis Menu ===")
        print("1. Filter by Card Category")
        print("2. Filter by State")
        print("3. Filter by Marital Status and Dependents")
        print("4. Filter by Loan Status and Age")
        print("0. Quit Program")

        choice = input("Enter your choice (1-4) or '0': ").strip()

        # Map choice to appropriate function
        if choice == '1':
            result = filter_by_card_category(csv_list)
        elif choice == '2':
            result = filter_by_state(csv_list)
        elif choice == '3':
            result = filter_by_marital_and_dependents(csv_list)
        elif choice == '4':
            result = filter_by_loan_and_age(csv_list)
        elif choice == '0':
            print("\nThank you for using our customer data explorer. Goodbye!")
            break  # End program
        else:
            print("Invalid choice. Please try again.")
            continue

        # Return to main menu if user chooses to quit within a filter
        if result == 'quit':
            print("Returning to main menu.\n")

# ------------------------------
# Entry point of the program
# ------------------------------
if __name__ == "__main__":
    main()


# In[ ]:




