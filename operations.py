
from read import inventory_table
import write

def sell_items(laptop_dictionary):
    """
    displays the inventory of laptops and allow customers to purchase items by selecting valid Id and available quantity.

    Arguments:
    laptops_dict (dict): A dictionary of laptops with ID no as keys and details of laptop as values.

    """

    #getting customer details first
    print("\nFor purchasing a laptop,please enter the details first.\n")
    customer_name = input("Name of the customer: ")
    while not customer_name.isalpha():
        print("Invalid name!Please enter correct name.")
        customer_name = input("Name of the customer: ")
    
    customer_phonenumber = input("Phone no: ")
    while not customer_phonenumber.isnumeric(): #isnumeric() if all the characters are numbers
        print("Your phone number is incorrect.")
        customer_phonenumber = input("Phone no: ")
    print("\n")

    # Initializing variables for shopping cart and loop for buying more items
    cart=[]
    buy_more_items="y"
    while buy_more_items == "y":

        #Show inventory and ask for laptop ID
        inventory_table()
        validlaptop_ID=0
        while validlaptop_ID<=0 or validlaptop_ID>len(laptop_dictionary):
            try:
                # get valid laptop ID
                validlaptop_ID = int(input("Enter the S.No of the laptop you want to purchase: "))
            except:
                print("Invalid Laptop ID. Please try again.")
                print("\n")
                continue
            if validlaptop_ID<=0 or validlaptop_ID>len(laptop_dictionary):
                print("ID not available. Please provide the ID of an available laptop only!\n")

        #get Valid quantity
        get_stock_of_selected_laptop=laptop_dictionary[validlaptop_ID][3]
        purchased_quantity=0
        while purchased_quantity<=0 or purchased_quantity>int(get_stock_of_selected_laptop):
            try:
                purchased_quantity=int(input("How many laptops would you like to purchase? "))
                print("\n")
            except:
                print("Invalid Quantity. Please try again.")
                print("\n")
            if purchased_quantity <=0:
                print("Invalid Quantity.Please try again.\n")
            elif purchased_quantity >int(get_stock_of_selected_laptop):
                print("Sorry",customer_name, "the quantity you are looking is not available at the moment.")
                print("\n")

        # Update the inventory with the purchased quantity
        laptop_dictionary[validlaptop_ID][3] = int(laptop_dictionary[validlaptop_ID][3]) - int(purchased_quantity)   
        write.update_stock(laptop_dictionary)

        # asking if the customer wants to buy more laptops
        buy_more_items = input("Do you want to buy another laptop as well? (y/n)").lower() 
        while not buy_more_items.isalpha():
            print("Invalid input. Please enter y or n.")
            buy_more_items = input("Do you want to buy another laptop as well? (y/n)").lower()
        print("\n")
        
        #getting user purchased items
        laptop_name=laptop_dictionary[validlaptop_ID][0]
        quantity_selected=(purchased_quantity)
        given_unitprice=laptop_dictionary[validlaptop_ID][2]
        price_of_selected_laptop=laptop_dictionary[validlaptop_ID][2].replace("$",'')
        total_price_of_selected_items=int(price_of_selected_laptop)*int(quantity_selected)  

        # Adding the purchased items to the cart       
        cart.append([laptop_name,quantity_selected,given_unitprice,total_price_of_selected_items])

    # asking user for shipping the items
    shipping_cost=input("Dear customer,do you want your laptop to be shipped?(y/n)").lower()
    print("\n")
    while not shipping_cost.isalpha():
        print("Invalid input. Please enter y or n.")
        shipping_cost=input("Dear customer,do you want your laptop to be shipped?(y/n)").lower()
    print("\n")

    # Getting input for shipping location if user chose shipping
    location=""
    if shipping_cost == "y":
        while not location.isalpha() or (location.lower() != "inside" and location.lower() != "outside"):
            location = input("Are you located inside or outside Kathmandu Valley? (Type 'inside' or 'outside'): ")
            print("\n")
            if not location.isalpha() or (location.lower() != "inside" and location.lower() != "outside"):
                print("Invalid location entered. Please enter 'inside' or 'outside'.\n")
    else:
        shipping_cost=0
        location=""

    #calling customer_bill to generate the bill  
    write.customer_bill(customer_name,customer_phonenumber,cart,shipping_cost,location)

    #calling write_sell_bill to write the bill in text file
    write.write_sell_bill(customer_name,customer_phonenumber,cart,shipping_cost,location)




def purchase_items(laptop_dictionary):
    """
    purchase_items(): displays the inventory of laptops after providing the distributor details and allows user to order items of available quantity with valid ID.

    Args: 
    laptop_dictionary: dictionary containing all the laptop information of Laptronix system.

    """ 

    #getting distributor details first
    print("\nFor ordering a laptop from manufacturer,fill up the required information first.\n")
    distributor_name = input("Name of the distributor: ")
    while not distributor_name.isalpha():
        print("Invalid name!Please enter correct name.")
        customer_name = input("Name of the distributor: ")
    
    distributor_phonenumber = input("Phone no: ")
    while not distributor_phonenumber.isnumeric():
        print("Your phone number is incorrect.")
        distributor_phonenumber = input("Phone no: ")
    print("\n")

    #Initializing variables for addtoshop list and loop for ordering more items
    addtoshop=[]
    order_more_items="y"
    while order_more_items == "y":
        inventory_table()
        laptop_ID=0
        while laptop_ID<=0 or laptop_ID>len(laptop_dictionary):
            try:
                # get valid laptop ID
                laptop_ID = int(input("Enter the Id of the laptop you want to order from manufacturer: "))
            except:
                print("Invalid Laptop ID. Please try again.")
                print("\n")
                continue
            if laptop_ID<=0 or laptop_ID>len(laptop_dictionary):
                print("ID not available. Please provide the ID of an available laptop only!\n")

        #get Valid quantity
        available_quantity=laptop_dictionary[laptop_ID][3]
        ordered_quantity=0
        while ordered_quantity<=0 or ordered_quantity>int(available_quantity):
            try:
                ordered_quantity=int(input("How many laptops would you like to order?: "))
                print("\n")
            except:
                print("Invalid Quantity. Please try again.")
                print("\n")
            if ordered_quantity <=0:
                print("Invalid Quantity.Please try again.\n")
            elif ordered_quantity >int(available_quantity):
                print("Sorry,the quantity you are looking is not available right now in our warehouse.")
                print("\n")

        # Update the Laptronix inventory by adding the purchased quantity
        laptop_dictionary[laptop_ID][3] = int(laptop_dictionary[laptop_ID][3]) + int(ordered_quantity)   
        write.update_stock(laptop_dictionary)

        order_more_items = input("Do you want to order more laptops? (y/n)").lower() 
        while not order_more_items.isalpha():
            print("Invalid input. Please enter y or n.")
            order_more_items = input("Do you want to order more laptops? (y/n)").lower()
        print("\n")
        
        #getting user purchased items
        laptop_name=laptop_dictionary[laptop_ID][0]
        quantity_selected=(ordered_quantity)
        given_unitprice=laptop_dictionary[laptop_ID][2]
        price_of_selected_laptop=laptop_dictionary[laptop_ID][2].replace("$",'')
        total_price_of_selected_items=int(price_of_selected_laptop)*int(quantity_selected)  

        # Adding the purchased items to the addtoshop list       
        addtoshop.append([laptop_name,quantity_selected,given_unitprice,total_price_of_selected_items])

    #calling customer_bill to generate the bill  
    write.distributor_invoice(distributor_name,distributor_phonenumber,addtoshop)

    #calling purchase_bill to write the invoice in file
    write.purchase_bill(distributor_name,distributor_phonenumber,addtoshop)
