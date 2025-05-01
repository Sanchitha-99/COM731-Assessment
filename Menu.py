#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# Import all task modules
from Task_A import *
from Task_B import *
from Task_C import *

def main_menu():
    # Initialize data variables
    csv_data = None  # For Task A
    df_data = None   # For Tasks B and C
    
    while True:
        print("\nMAIN MENU")
        print("1. Task A - Customer Data Filtering")
        print("2. Task B - Customer Data Analysis")
        print("3. Task C - Customer Data Visualization")
        print("4. Load Data Files")
        print("5. Exit Program")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            if csv_data is None:
                print("\nPlease load the data first using option 4")
                continue
            task_a_menu(csv_data)
        elif choice == '2':
            if df_data is None:
                print("\nPlease load the data first using option 4")
                continue
            task_b_menu(df_data)
        elif choice == '3':
            if df_data is None:
                print("\nPlease load the data first using option 4")
                continue
            task_c_menu(df_data)
        elif choice == '4':
            csv_data, df_data = load_data_files()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")

def load_data_files():
    """Load data for all tasks at once"""
    print("\nLoading data files...")
    
    # Load data for Task A
    csv_data = load_csv_file()
    if csv_data is None:
        return None, None
    
    # Load data for Tasks B and C
    try:
        df_data = load_customer_data("credit_card_customers.csv")  # Using the filename from the modules
        print("Data loaded successfully for all tasks!")
        return csv_data, df_data
    except Exception as e:
        print(f"Error loading data for Tasks B/C: {e}")
        return csv_data, None

def task_a_menu(csv_list):
    while True:
        print("\nTASK A MENU - Customer Data Filtering")
        print("1. Filter by Card Category")
        print("2. Filter by State")
        print("3. Filter by Marital Status and Dependents")
        print("4. Filter by Loan and Age")
        print("5. Return to Main Menu")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            result = filter_by_card_category(csv_list)
            if result == 'quit':
                return
        elif choice == '2':
            result = filter_by_state(csv_list)
            if result == 'quit':
                return
        elif choice == '3':
            result = filter_by_marital_and_dependents(csv_list)
            if result == 'quit':
                return
        elif choice == '4':
            result = filter_by_loan_and_age(csv_list)
            if result == 'quit':
                return
        elif choice == '5':
            return
        else:
            print("Invalid choice. Please enter a number between 1-5.")

def task_b_menu(df):
    while True:
        print("\nTASK B MENU - Customer Data Analysis")
        print("1. Analyze Top Jobs by Card Category")
        print("2. Analyze Average Fee and Income")
        print("3. Analyze Average Fee by Marital Status")
        print("4. Analyze Interest and Credit Limit")
        print("5. Return to Main Menu")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            analyze_top_jobs(df)
        elif choice == '2':
            analyze_avg_fee_and_income(df)
        elif choice == '3':
            analyze_avg_fee_by_marital_status(df)
        elif choice == '4':
            analyze_interest_and_limit(df)
        elif choice == '5':
            return
        else:
            print("Invalid choice. Please enter a number between 1-5.")

def task_c_menu(df):
    while True:
        print("\nTASK C MENU - Customer Data Visualization")
        print("1. Card Type Distribution by Education Level")
        print("2. Monthly Interest Trend by Card Category")
        print("3. Compare Annual Fees vs Acquisition Costs")
        print("4. Stacked Expense Type Distribution")
        print("5. Return to Main Menu")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            show_card_type_distribution(df)
        elif choice == '2':
            plot_monthly_interest_trend(df)
        elif choice == '3':
            compare_avg_fees_and_acquisition_costs(df)
        elif choice == '4':
            plot_stacked_expense_type_distribution(df)
        elif choice == '5':
            return
        else:
            print("Invalid choice. Please enter a number between 1-5.")

# Start the program
if __name__ == "__main__":
    print("Welcome to Customer Data Analysis Program!")
    print("Please load the data files first using option 4 in the main menu.")
    main_menu()


# In[ ]:





# In[ ]:




