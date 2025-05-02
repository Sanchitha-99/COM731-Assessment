#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Import all task modules with aliases
import Retrieving_Data_Module as RDM
import Filtering_Data_Module as FDM
import Visualizing_Data_Module as VDM

def main_menu():
    # Initialize data variables
    csv_data = None  # For Task A (Retrieving Data)
    df_data = None   # For Tasks B and C (Filtering and Visualizing)
    
    while True:
        print("\n=== CUSTOMER DATA ANALYSIS SYSTEM ===")
        print("1. Task A - Data Retrieval")
        print("2. Task B - Data Filtering")
        print("3. Task C - Data Visualization")
        print("4. Load Data Files")
        print("0. Exit Program")
        
        choice = input("Enter your choice (0-4): ").strip()
        
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
        elif choice == '0':
            print("\nThank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0-4.")

def load_data_files():
    """Load data for all tasks at once"""
    print("\nLoading data files...")
    
    # Load data for Task A (Retrieving Data)
    csv_data = RDM.load_csv_file()
    if csv_data is None:
        return None, None
    
    # Load data for Tasks B and C (Filtering and Visualizing)
    try:
        df_data = FDM.load_customer_data()
        if df_data is not None:
            print("Data loaded successfully for all tasks!")
        return csv_data, df_data
    except Exception as e:
        print(f"Error loading data for Tasks B/C: {e}")
        return csv_data, None

def task_a_menu(csv_list):
    while True:
        print("\n=== DATA RETRIEVAL MENU ===")
        print("1. Filter by Card Category")
        print("2. Filter by State")
        print("3. Filter by Marital Status and Dependents")
        print("4. Filter by Loan and Age")
        print("0. Return to Main Menu")
        
        choice = input("Enter your choice (0-4): ").strip()
        
        if choice == '1':
            RDM.filter_by_card_category(csv_list)
        elif choice == '2':
            RDM.filter_by_state(csv_list)
        elif choice == '3':
            RDM.filter_by_marital_and_dependents(csv_list)
        elif choice == '4':
            RDM.filter_by_loan_and_age(csv_list)
        elif choice == '0':
            return
        else:
            print("Invalid choice. Please enter a number between 0-4.")

def task_b_menu(df):
    while True:
        print("\n=== DATA FILTERING MENU ===")
        print("1. Analyze Top Jobs by Card Category")
        print("2. Analyze Average Fee and Income")
        print("3. Analyze Average Fee by Marital Status")
        print("4. Analyze Interest and Credit Limit")
        print("0. Return to Main Menu")
        
        choice = input("Enter your choice (0-4): ").strip()
        
        if choice == '1':
            FDM.analyze_top_jobs(df)
        elif choice == '2':
            FDM.analyze_avg_fee_and_income(df)
        elif choice == '3':
            FDM.analyze_avg_fee_by_marital_status(df)
        elif choice == '4':
            FDM.analyze_interest_and_limit(df)
        elif choice == '0':
            return
        else:
            print("Invalid choice. Please enter a number between 0-4.")

def task_c_menu(df):
    while True:
        print("\n=== DATA VISUALIZATION MENU ===")
        print("1. Card Type Distribution by Education Level")
        print("2. Monthly Interest Trend by Card Category")
        print("3. Compare Annual Fees vs Acquisition Costs")
        print("4. Customers per Expense Type")
        print("0. Return to Main Menu")
        
        choice = input("Enter your choice (0-4): ").strip()
        
        if choice == '1':
            VDM.show_card_type_distribution(df)
        elif choice == '2':
            VDM.plot_monthly_interest_trend(df)
        elif choice == '3':
            VDM.compare_avg_fees_and_acquisition_costs(df)
        elif choice == '4':
            VDM.plot_avg_customers_per_expense_type(df)
        elif choice == '0':
            return
        else:
            print("Invalid choice. Please enter a number between 0-4.")

# Start the program
if __name__ == "__main__":
    print("Welcome to Customer Data Analysis System!")
    print("Please load the data files first using option 4 in the main menu.")
    main_menu()


# In[ ]:





# In[ ]:




