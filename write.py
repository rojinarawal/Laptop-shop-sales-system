
from datetime import datetime

def update_stock(laptop_dictionary):
    """
    update_stock(): updates the laptop data with the purchased or sold quantity and returns a dictionary with laptop id as key and datas as value.

    Returns:
        laptop_dictionary: A dictionary with laptop id as key and  laptop data as values.
    """
    #update the text file
    
    file = open("laptopshop.txt","w")

    for values in laptop_dictionary.values():
        file.write(str(values[0])+ "," + str(values[1])+ ","+ str(values[2] )+ ","+ str(values[3])+","+str(values[4])+","+str(values[5])+","+str(values[6]))
        file.write("\n")
    file.close()
    return laptop_dictionary



def customer_bill(customer_name,customer_phonenumber,cart,shipping_cost,location):
    """
    customer_bill(): generates the customer bill after the laptops being sold 

    Args:
        - customer_name (str): name of the customer.
        - customer_phonenumber (int/str):  phone number of the customer.
        - cart (list): A list of items in the customer's shopping cart, where each item is represented as a tuple 
                        of four values: (product description, quantity, unit price, total price).
        - shipping_cost (int): The shipping cost to be added to the total cost.
        - location (str): The location of the customer's address, either 'inside' or 'outside'. 
    """

    #if customer chooses shipping ,shipping_cost is charged according to the locations
    if shipping_cost == 'y':
        if location.lower() == 'inside':
            shipping_cost = 100
        else:
            shipping_cost = 150
    else:
        shipping_cost=0 

    #initializing total_cost to store the cost of customer purchased items
    total_cost=0
    for i in cart:
        total_cost += int(i[3])
    grand_cost = total_cost+shipping_cost #cost with shipping charge

    recent_date_and_time=datetime.now()
    print("\n")
    print("+=======================================================================================+")
    print("\t\t\t\tLAPTRONIX BILL")
    print("+=======================================================================================+")
    print("\n\t\t\t   Ghorahi, Dang  |  Phone No: 01-5415142 ")
    print("-----------------------------------------------------------------------------------------")
    print("BILL TO")
    print("-----------------------------------------------------------------------------------------")
    print("Customer name: "+str(customer_name))
    print("Cell/Phone: "+str(customer_phonenumber))
    print("Purchased Date and time: "+ str(recent_date_and_time))
    print("\n")
    print("Purchase Details:")
    print("+---------------------------------------------------------------------------------------+") 
    print("\tS.NO \t PRODUCT DESCRIPTION \t\t QTY \t\t UNIT PRICE \t TOTAL")
    print("+---------------------------------------------------------------------------------------+")

    #displaying the purchase details in the bill    
    a= 1 #a denotes the S.No
    for i in cart:
        print("\t",a,"\t",i[0],"\t\t\t",i[1],"\t\t",i[2],"\t\t$",i[3])
        a = a+1
    print("+---------------------------------------------------------------------------------------+")
    print("\n")
    
    if shipping_cost > 0: 
        #converting the integer values into string and displaying them
        print("Your Shipping Cost is: $"+str(shipping_cost)) 
        print("Grand Total: $"+str(grand_cost))
        print("Note: **Shipping cost is added to Grand Total**")
    else:
        print("Grand Total: $"+str(total_cost))
    print("\n")


    
def write_sell_bill(customer_name,customer_phonenumber,cart,shipping_cost,location):
    """
    This function takes in the customer's name, phone no, shopping cart items, shipping cost, and location 
    as inputs and writes a bill with all the necessary details in a text file.]

    Parameters passed:
         customer_name,customer_phonenumber,cart,shipping_cost,location
    """
    recent_date_and_time=datetime.now()

    # Open a text file with the customer's name and phone number
    with open(str(customer_name) + str(customer_phonenumber) + ".txt", "w") as file:
        file.write("\n")
        file.write("+=======================================================================================+\n")
        file.write("\t\t\t\t\tLAPTRONIX BILL\n")
        file.write("+=======================================================================================+\n")
        file.write("\t\t\t   Ghorahi, Dang  |  Phone No: 01-5415142 \n")
        file.write("-----------------------------------------------------------------------------------------\n")
        file.write("BILL TO\n")
        file.write("-----------------------------------------------------------------------------------------\n")
        file.write("Customer name: "+str(customer_name)+"\n")
        file.write("Cell/Phone: "+str(customer_phonenumber)+"\n")
        file.write("Purchased Date and time: "+ str(recent_date_and_time)+"\n")
        file.write("\n")
        file.write("\nPurchase Details:\n\n")
        file.write("+---------------------------------------------------------------------------------------+\n") 
        file.write("\tS.NO \t PRODUCT DESCRIPTION \t\t QTY \t\t UNIT PRICE \t TOTAL\n")
        file.write("+---------------------------------------------------------------------------------------+\n")

        #Writing the details of each item in the cart   
        a= 1 #a denotes the S.No
        total_cost=0
        for i in cart:
            total_cost += i[3]
            file.write("\t" + str(a) + "\t\t" + str(i[0]) + "\t\t\t\t\t" + str(i[1]) + "\t\t\t" + str(i[2]) + "\t\t\t" + "$" + str(i[3]) + "\n")
            a = a+1
        file.write("+---------------------------------------------------------------------------------------+\n")
        file.write("\n\n")
        
        # displays the shipping cost according to location and grand total
        if location.lower() == 'inside':
            shipping_cost = 100
        else:
            shipping_cost = 150

        grand_cost = total_cost+shipping_cost    
        if shipping_cost > 0:
            file.write("Your Shipping Cost is: $"+str(shipping_cost)+"\n")
            file.write("Grand Total: $"+str(grand_cost)+"\n")
            file.write("Note: **Shipping cost is added to Grand Total**\n")
        else:
            file.write("Grand Total: $"+str(total_cost)+"\n")
        file.write("\n")



def distributor_invoice(distributor_name,distributor_phonenumber,addtoshop):
    """
    Generates an invoice of items ordered from distributor.

    Parameters:
    - distributor_name (str): name of the distributor.
    - distributor_phonenumber (str): phone number of the distributor.
    - addtoshop (list): list of purchased items.
    """


    net_amount=0
    # Calculating the total net amount by iterating through the purchased items
    for i in addtoshop:
        net_amount += int(i[3])

    # Calculating the VAT amount and the gross amount    
    Vat_amount = 0.13*net_amount
    gross_amount = net_amount+Vat_amount

    # Generating the invoice
    purchase_date_and_time=datetime.now()
    print("\n")
    print("+=======================================================================================+")
    print("\t\t\t\tLAPTRONIX BILL")
    print("+=======================================================================================+")
    print("\n\t\t\t   Ghorahi, Dang  |  Phone No: 01-5415142 ")
    print("-----------------------------------------------------------------------------------------")
    print("BILL TO")
    print("-----------------------------------------------------------------------------------------")
    print("Distributor/Company name: "+str(distributor_name))
    print("Contact: "+str(distributor_phonenumber))
    print("Purchased Date and time: "+ str(purchase_date_and_time))
    print("\n")
    print("Order Details:")
    print("+---------------------------------------------------------------------------------------+") 
    print("\tS.NO \t LAPTOP NAME \t\t QTY \t\t UNIT PRICE \t TOTAL")
    print("+---------------------------------------------------------------------------------------+")

    #displaying the purchase details in the bill    
    a= 1 #a denotes the S.No
    for i in addtoshop:
        print("\t",a,"\t",i[0],"\t\t",i[1],"\t\t",i[2],"\t\t$",i[3])
        a = a+1
    print("+---------------------------------------------------------------------------------------+")
    print("\n\n")
    
    print("Net Amount : $"+str(net_amount)+"\n")
    print("Vat Added : 13%"+"\n")
    print("Vat Amount: $"+str(Vat_amount)+"\n")
    print("Gross Amount: $"+str(gross_amount)+"\n")



def purchase_bill(distributor_name,distributor_phonenumber,addtoshop):
    """
    Generates a text file bill for the ordered items from distributor.

    Parameters:
    - distributor_name (str)
    - distributor_phonenumber (str)
    - addtoshop (list):  list of purchased items.

    Returns:
    - None
    """

    # Generating the text file bill
    purchase_date_and_time=datetime.now()
    file=open(str(distributor_name)+str(distributor_phonenumber)+".txt","w")
    file.write("\n")
    file.write("+=======================================================================================+\n")
    file.write("\t\t\t\tLAPTRONIX BILL\n")
    file.write("+=======================================================================================+\n")
    file.write("\t\t\t   Ghorahi, Dang  |  Phone No: 01-5415142 \n")
    file.write("-----------------------------------------------------------------------------------------\n")
    file.write("BILL TO\n")
    file.write("-----------------------------------------------------------------------------------------\n")
    file.write("Distributor/Company name: "+str(distributor_name)+"\n")
    file.write("Contact: "+str(distributor_phonenumber)+"\n")
    file.write("Purchased Date and time: "+ str(purchase_date_and_time)+"\n")
    file.write("\n")
    file.write("Order Details: \n")
    file.write("+---------------------------------------------------------------------------------------+\n") 
    file.write("\tS.NO \t LAPTOP NAME \t\t QTY \t\t UNIT PRICE \t TOTAL\n")
    file.write("+---------------------------------------------------------------------------------------+\n")
    net_amount=0
    a= 1
    for i in addtoshop:
        net_amount += int(i[3])
        #displaying the purchase details in the invoice    
        file.write("\t" + str(a) + "\t\t" + str(i[0]) + "\t\t\t" + str(i[1]) + "\t\t\t" + str(i[2]) + "\t\t\t" + "$" + str(i[3]) + "\n")
        a = a+1
    file.write("+---------------------------------------------------------------------------------------+\n")
    file.write("\n\n")
    Vat_amount = 0.13*net_amount
    gross_amount = net_amount+Vat_amount
    file.write("Net Amount : $"+str(net_amount)+"\n")
    file.write("Vat Added : 13%"+"\n")
    file.write("Vat Amount: $"+str(Vat_amount)+"\n")
    file.write("Gross Amount: $"+str(gross_amount)+"\n")
    file.close()
