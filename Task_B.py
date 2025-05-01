#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# customer_analysis.py
import pandas as pd

# Load the data (moved to a function for module use)
def load_customer_data():
    try:
        file_path = "credit_card_customers.csv"
        df = pd.read_csv(file_path, header=0, encoding='utf-8')
        print("Credit Card Customers data frame loaded successfully.")
        return df
    except FileNotFoundError as e1:
        print(f"File not found - {e1}")
        return None
    except Exception as e2:
        print(f"Exception - {e2}")
        return None

# --- B1 Function ---
def analyze_top_jobs(df):
    if 'Card_Category' not in df.columns or 'Income' not in df.columns or 'Customer_Job' not in df.columns:
        print("Required columns are missing from the dataset.")
        return

    valid_card_types = sorted(df['Card_Category'].dropna().unique())

    while True:
        print("\nAvailable Card Types:")
        for idx, card in enumerate(valid_card_types, 1):
            print(f"{idx}. {card}")

        card_input = input("Select a card type by number (or type 'quit' to exit): ").strip()
        if card_input.lower() == 'quit':
            print("Exiting B1...")
            break

        if not card_input.isdigit() or not (1 <= int(card_input) <= len(valid_card_types)):
            print("Invalid selection. Please try again.")
            continue

        selected_card = valid_card_types[int(card_input) - 1]
        filtered = df.loc[(df['Card_Category'] == selected_card) & (df['Income'] > 100000)]

        if filtered.empty:
            print("No matching records found.")
        else:
            top_jobs = filtered['Customer_Job'].value_counts().head(3)
            print(f"\nTop 3 Occupations for '{selected_card}' card holders with income > $100,000:")
            print(top_jobs)

        again = input("\nWould you like to run this analysis again? (yes/no): ").strip().lower()
        if again != 'yes':
            break

# --- B2 Function ---
def analyze_avg_fee_and_income(df):
    if 'Customer_Job' not in df.columns or 'Card_Category' not in df.columns:
        print("Required columns are missing from the dataset.")
        return

    valid_occupations = df['Customer_Job'].dropna().unique()
    valid_card_types = df['Card_Category'].dropna().unique()

    while True:
        print("\nAvailable Occupations:")
        for idx, occupation in enumerate(valid_occupations, 1):
            print(f"{idx}. {occupation}")

        occupation = input("Select an occupation by number (or type 'quit'): ").strip()
        if occupation.lower() == 'quit':
            print("Exiting B2...")
            break
        if not occupation.isdigit() or not (1 <= int(occupation) <= len(valid_occupations)):
            print("Invalid selection.")
            continue

        selected_occupation = valid_occupations[int(occupation) - 1]

        print("\nAvailable Card Types:")
        for idx, card in enumerate(valid_card_types, 1):
            print(f"{idx}. {card}")

        card_input = input("Select a card type by number (or type 'quit'): ").strip()
        if card_input.lower() == 'quit':
            break
        if not card_input.isdigit() or not (1 <= int(card_input) <= len(valid_card_types)):
            print("Invalid selection.")
            continue

        selected_card = valid_card_types[int(card_input) - 1]
        filtered = df.loc[(df['Customer_Job'] == selected_occupation) & (df['Card_Category'] == selected_card)]

        if not filtered.empty:
            avg_values = filtered[['Annual_Fees', 'Income']].mean()
            print(f"\nAverage annual credit card fee and income for '{selected_occupation}' & '{selected_card}':")
            print(avg_values)
        else:
            print("No matching records found.")

        again = input("\nWould you like to run this analysis again? (yes/no): ").strip().lower()
        if again != 'yes':
            break

# --- B3 Function ---
def analyze_avg_fee_by_marital_status(df):
    required_columns = ['Education_Level', 'House_Owner', 'Income', 'Marital_Status', 'Annual_Fees']
    if not all(col in df.columns for col in required_columns):
        print("Some required columns are missing from the dataset.")
        return

    education_levels = df['Education_Level'].dropna().unique()
    home_ownership = df['House_Owner'].dropna().unique()
    marital_status = df['Marital_Status'].dropna().unique()

    while True:
        print("\nAvailable Education Levels:")
        for idx, level in enumerate(education_levels, 1):
            print(f"{idx}. {level}")

        edu_input = input("Select Education Level (number or 'quit'): ").strip()
        if edu_input.lower() == 'quit':
            break
        if not edu_input.isdigit() or not (1 <= int(edu_input) <= len(education_levels)):
            print("Invalid input.")
            continue
        selected_edu = education_levels[int(edu_input) - 1]

        home_input = input("Do you own a home? (yes/no or 'quit'): ").strip().lower()
        if home_input == 'quit':
            break
        if home_input not in ['yes', 'no']:
            print("Invalid home ownership input.")
            continue

        income_input = input("Enter minimum income threshold (numeric or 'quit'): ").strip()
        if income_input.lower() == 'quit':
            break
        try:
            income_threshold = float(income_input)
        except ValueError:
            print("Invalid income input.")
            continue

        filtered = df.loc[(df['Education_Level'] == selected_edu) &
                         (df['House_Owner'].str.lower() == home_input) &
                         (df['Income'] > income_threshold)]
        if filtered.empty:
            print("No records found.")
            continue

        print("\nAvailable Marital Statuses:")
        for idx, status in enumerate(marital_status, 1):
            print(f"{idx}. {status}")

        marital_input = input("Select Marital Status (number or 'quit'): ").strip()
        if marital_input.lower() == 'quit':
            break
        if not marital_input.isdigit() or not (1 <= int(marital_input) <= len(marital_status)):
            print("Invalid selection.")
            continue

        selected_status = marital_status[int(marital_input) - 1]
        final_filtered = filtered[filtered['Marital_Status'] == selected_status]

        if final_filtered.empty:
            print("No records for this marital status.")
        else:
            avg_fee = final_filtered['Annual_Fees'].mean()
            print(f"\nAverage Annual Fee for '{selected_status}' customers: ${avg_fee:.2f}")

        again = input("\nWould you like to run this analysis again? (yes/no): ").strip().lower()
        if again != 'yes':
            break

# --- B4 Function ---
def analyze_interest_and_limit(df):
    required_columns = ['Customer_Job', 'Exp Type', 'Personal_loan', 'Car_Owner', 'Interest_Earned', 'Credit_Limit']
    if not all(col in df.columns for col in required_columns):
        print("Some required columns are missing from the dataset.")
        return

    employment_statuses = df['Customer_Job'].dropna().unique()
    expense_types = df['Exp Type'].dropna().unique()

    while True:
        print("\nEmployment Status Options:")
        for i, job in enumerate(employment_statuses, 1):
            print(f"{i}. {job}")
        emp_input = input("Select Employment Status (number or 'quit'): ").strip()
        if emp_input.lower() == 'quit':
            break
        if not emp_input.isdigit() or not (1 <= int(emp_input) <= len(employment_statuses)):
            print("Invalid input.")
            continue
        selected_job = employment_statuses[int(emp_input) - 1]

        loan_input = input("Do you have a loan? (yes/no): ").strip().lower()
        car_input = input("Do you own a car? (yes/no): ").strip().lower()
        if loan_input not in ['yes', 'no'] or car_input not in ['yes', 'no']:
            print("Invalid loan or car input.")
            continue

        print("\nExpense Type Options:")
        for i, etype in enumerate(expense_types, 1):
            print(f"{i}. {etype}")
        exp_input = input("Select Expense Type (number or 'quit'): ").strip()
        if exp_input.lower() == 'quit':
            break
        if not exp_input.isdigit() or not (1 <= int(exp_input) <= len(expense_types)):
            print("Invalid expense type.")
            continue
        selected_exp = expense_types[int(exp_input) - 1]

        custom_filtered = df.loc[
            (df['Customer_Job'] == selected_job) &
            (df['Personal_loan'].str.lower() == loan_input) &
            (df['Car_Owner'].str.lower() == car_input) &
            (df['Exp Type'] == selected_exp)
        ]

        if custom_filtered.empty:
            print("No matching records found.")
        else:
            avg_interest = custom_filtered['Interest_Earned'].mean()
            avg_limit = custom_filtered['Credit_Limit'].mean()
            print(f"\nAverage Interest Earned: ${avg_interest:.2f}")
            print(f"Average Credit Limit: ${avg_limit:.2f}")

        again = input("\nWould you like to run this analysis again? (yes/no): ").strip().lower()
        if again != 'yes':
            break

# --- Main menu for use as a standalone script ---
def filtering_customers_information(df):
    while True:
        print("\n=== Credit Card Analysis Menu ===")
        print("1. Top Jobs for High-Income Cardholders (B1)")
        print("2. Avg Annual Fee & Income by Occupation/Card (B2)")
        print("3. Avg Annual Fee by Marital Status (B3)")
        print("4. Interest and Credit Limit Analysis (B4)")
        print("0. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            analyze_top_jobs(df)
        elif choice == '2':
            analyze_avg_fee_and_income(df)
        elif choice == '3':
            analyze_avg_fee_by_marital_status(df)
        elif choice == '4':
            analyze_interest_and_limit(df)
        elif choice == '0':
            print("\nThank you for using our customer data explorer. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from the menu.")

# Allow standalone execution
if __name__ == "__main__":
    filtering_customers_information(df_ccards)


# In[ ]:





# In[ ]:





# In[ ]:




