#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv

def main():
    print("Loading...")
    print("Importing the main file credit_card_customers.csv")

    # Empty list to store data
    csv_list = []

    while True:
        file_name = input("Enter the CSV file name or enter 'q' to quit the program: ")

        # If input is 'q', exit the program
        if file_name.lower() == 'q':
            print("Exiting the program.")
            break  # Exit loop

        try:
            # Open the CSV file
            with open(file_name, 'r', encoding='UTF-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                # Clear csv_list before storing new data
                csv_list.clear()

                # Read and store data
                for row in csv_reader:
                    csv_list.append(row)

            print("CSV file loaded successfully.")
            break  # Exit loop after successfully reading the file

        except FileNotFoundError:
            print(f"File '{file_name}' does not exist. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




