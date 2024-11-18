# Throughout this project, the use of data structures are not permitted 
# Minimal built in functions are to be used and the majority of functions must be
# created yourself

# More packages may be imported in the space below if approved by your instructor
import csv

def printMenu():
    print('''
          Customer and Sales System\n
          1. Enter Customer Information\n
          2. Generate Customer data file\n
          3. Report on total Sales (Not done in this part)\n
          4. Check for fraud in sales data (Not done in this part)\n
          9. Quit\n
          Enter menu option (1-9)
          ''')

def enterCustomerInfo():
    global customer_list
    customer = {}

    # Get the customer's information
    customer['First Name'] = input("Enter first name: ")
    customer['Last Name'] = input("Enter last name: ")
    customer['City'] = input("Enter city: ")

    # Get the customer's postal code and validate it
    postal_code = input("Enter postal code: ")
    while not validatePostalCode(postal_code):
        print("Invalid postal code. Please try again.")
        postal_code = input("Enter postal code: ")
    customer['Postal Code'] = postal_code

    # Get the customer's credit card and validate it
    credit_card = input("Enter credit card number: ")
    while not validateCreditCard(credit_card):
        print("Invalid credit card number. Please try again.")
        credit_card = input("Enter credit card number: ")
    customer['Credit Card'] = credit_card

    # assign the customer an id
    customer['ID'] = len(customer_list) + 1

    # add the customer to the list
    customer_list.append(customer)
    print("Customer information added successfully.")

def validatePostalCode(postal_code):
    # first, ensure the postal code is longer than 3 characters
    if len(postal_code) < 3:
        return False    

    # read the postal_codes.csv file
    with open('postal_codes.csv', 'r', encoding='ISO-8859-1') as file:
        reader = csv.reader(file, delimiter='|')
        
        for row in reader: # iterate through each row and check if the postal code matches
            if postal_code[:3] == row[0]:
                return True
    return False

def validateCreditCard(card_number):
    # ensure the credit card number is longer than 9 characters
    if len(card_number) < 9 or not card_number.isdigit():
        return False

    # reverse the card number
    card_number_reversed = card_number[::-1]
    sum1, sum2 = 0, 0

    for i, digit in enumerate(card_number_reversed):
        num = int(digit)
        # Perform a partial sum of the odd digits
        if i % 2 == 0:
            sum1 += num
        else:
            doubled = num * 2 # multiply each digit by two and sum them
            sum2 += doubled if doubled < 10 else doubled - 9 # if the answer is greater than 9 then add the 2 digits to form partial sums for the even digits
    
    # If sum1 + sum2 ends in zero then the original number is valid, otherwise it is invalid.
    return (sum1 + sum2) % 10 == 0



def generateCustomerDataFile():
    global customer_list
    file_name = "customers.csv"
    
    # Overwrite the file ('w') with the current customer list
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header
        writer.writerow(["ID", "First Name", "Last Name", "City", "Postal Code", "Credit Card"])

        # Write all customers from the list
        for customer in customer_list:
            writer.writerow([
                customer['ID'],
                customer['First Name'],
                customer['Last Name'],
                customer['City'],
                customer['Postal Code'],
                customer['Credit Card']
            ])
    
    print(f"Customer data has been saved to {file_name}.")



####################################################################
#       ADDITIONAL METHODS MAY BE ADDED BELOW IF NECESSARY         #
####################################################################

def loadCustomerData():
    global customer_list
    file_name = "customers.csv"
    
    try:
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                customer = {
                    'ID': int(row[0]),
                    'First Name': row[1],
                    'Last Name': row[2],
                    'City': row[3],
                    'Postal Code': row[4],
                    'Credit Card': row[5]
                }
                customer_list.append(customer)
    except FileNotFoundError:
        print(f"{file_name} not found. Starting with an empty customer list.")
    except Exception as e:
        print(f"Error reading {file_name}: {e}")


####################################################################
#                            MAIN PROGRAM                          #
#           DO NOT EDIT ANY CODE EXCEPT WHERE INDICATED            #
####################################################################

# Do not edit any of these variables
userInput = ""
enterCustomerOption = "1"
generateCustomerOption = "2"
exitCondition = "9"

# More variables for the main may be declared in the space below

customer_list = []


# Code

loadCustomerData()

while userInput != exitCondition:
    printMenu()                 # Printing out the main menu
    userInput = input();        # User selection from the menu

    if userInput == enterCustomerOption:
        # Only the line below may be editted based on the parameter list and how you design the method return
        # Any necessary variables may be added to this if section, but nowhere else in the code
        enterCustomerInfo()

    elif userInput == generateCustomerOption: 
        # Only the line below may be editted based on the parameter list and how you design the method return
        generateCustomerDataFile()

    else:
        print("Please type in a valid option (A number from 1-9)")

#Exits once the user types 
print("Program Terminated")