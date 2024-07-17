def inventory():
    """
    inventory(): reads the laptop data laptopshop file and returns a dictionary with laptop id as key and datas as value.

    Returns:
        laptop_dictionary: A dictionary with laptop id as key and  laptop data as values.
    """

    file=open("laptopshop.txt","r")   #opens the file in read mode
    laptop_dictionary={}   #empty dictionary to store the laptop data  
    laptop_id=1     #initializing the laptop_id to 1
    for line in file: 
        line=line.replace("\n","")  #removing the newline from line
        laptop_dictionary.update({laptop_id: line.split(",")}) #adding the datas to dictionary with l_id as key
        laptop_id=laptop_id+1
    file.close()
    return laptop_dictionary



def inventory_table():
    """
    inventory_table(): reads the laptop data from lapshop.txt file and displays it in the form of a table.

    """
    print("\n\n___________________________________________________________________________________________________________________________________\n")
    print("\t\t\t\tDiscover the laptop that matches your style and needs!")
    print("___________________________________________________________________________________________________________________________________")
    print("-----------------------------------------------------------------------------------------------------------------------------------")       
    print("S.N\tLaptop name  \t  Brand \t Price\t Stock\t Processor  \t Graphics\t Storage")
    print("-----------------------------------------------------------------------------------------------------------------------------------") 

    file = open("laptopshop.txt", "r")
    a= 1 #a denotes the S.No
    for line in file:
        values = line.strip().split(",") #using strip to remove new lines and splitting the data with comma
        print( a,"\t"+values[0]+"\t",values[1]+"\t\t",values[2]+"\t",values[3]+"\t",values[4]+"\t",values[5]+"\t",values[6]+"\t") #displaying values in table
        a= a+1
    file.close()
    print("-----------------------------------------------------------------------------------------------------------------------------------\n\n")
