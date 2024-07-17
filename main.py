import read # importing the read and operations module in main file
import operations


# Prints the welcome message for LapTronix system
print("\n\n")
print("\t\t\t\t\t\t ***             ***")
print("\t\t\t\t\t\t *     LapTronix   *")
print("\t\t\t\t\t\t *_________________*")
print("\n\t\t\t\t\t   Ghorahi, Dang  |  Phone No: 01-5415142 ")
print("\n")
print("-----------------------------------------------------------------------------------------------------------------------------------")
print("\t\t\t\t Welcome to the Laptronix system, dear Admin! Have a good day ahead!")
print("-----------------------------------------------------------------------------------------------------------------------------------")
print("\n")


# calling the inventory function to display laptop_dictionary 
laptop_dictionary=read.inventory()
print(laptop_dictionary)

#Starting the loop
loop=True
while loop==True:
    print("\n\n")
    print("Please select from the following options to get started: ")
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print("\nTo sell a laptop to a customer, please press 1.")
    print("To purchase a laptop from a manufacturer, please press 2.")
    print("To exit the system, please press 3.\n")
    print("-----------------------------------------------------------------------------------------------------------------------------------")

    user_input = input("Which option would you like to choose?: ")

    # is numeric() function is use to make sure that user inputs the numbers only in options menu.
    if user_input.isnumeric():
        user_input = int(user_input) 

        #it calls the function of selling from operations module
        if user_input == 1:
            operations.sell_items(laptop_dictionary)
            print("\n")

        #purchase laptop from company function is called here     
        elif user_input == 2:
            operations.purchase_items(laptop_dictionary)
            print("\n")
        
        #if user chooses 3 loop will break
        elif user_input == 3:
            loop = False
            print("Thank you for visiting the Laptronix store, have a good day.")
            break

        else:
            print("Your option", user_input, "doesn't seem to be available in our system. Please try again.")
            print("\n")
    else:
        print("Invalid input! Please enter a number from the available options.")
