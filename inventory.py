#Capstone Project IV - OOP
#Engineer: Jarache Khunyeli
#Student Number: JS22110005406
#Level 1; Task 30

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):

        return float(self.cost)

    def get_quantity(self):

        return int(self.quantity)

    def __str__(self):

        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}\n"


#==========Functions outside the class==============

shoe_list = []


# Define function 'read_shoes_data'
#   Within 'try - except' block, either read file contents and store data as list of objects
#   or raise appropriate error message should file not be found.
def read_shoes_data():
    try:
        with open("L1_caps/inventory.txt", "r") as file_contents:
            file = file_contents.readlines()[1:]
            for line in file:
                temp = line.strip().split(",")
                shoe_list.append(Shoe(temp[0], temp[1], temp[2], temp[3], temp[4]))
    except FileNotFoundError:
        print('''The file (inventory.txt) does not exist. To correct this, you can:
- Check the file name
- Make sure that the file is stored in the same folder as this program.\n''')


# Define 'capture_shoes' function
#   obtain required data from user & ensure value types are adhered to using 'try - except' block.
def capture_shoes():
    while True:
        try:
            new_country = input("Enter the country from which the shoe originates: ")
            new_code = input("Enter the shoe's product code (8 characters): ")
            new_prod_name = input("Enter the name of the product: ")
            new_cost = int(input("Enter the cost (rounded off to the nearest rand) of each pair of this shoe: "))
            new_quantity = int(input("Enter the number of pairs to be added to the inventory: "))
            for i in range(len(shoe_list)):
                if new_code.upper() == shoe_list[i].code.lower():
                    print('''The product code you've entered already exists.
    Check inventory list (from 'main menu' >>> type 's' >>> enter product code).''')
                    return
            else:
                shoe_list.append(Shoe(new_country, new_code, new_prod_name, new_cost, new_quantity))
                with open("L1_caps/inventory.txt", "a") as add_shoe:
                    add_shoe.write(f'''\n{new_country},{new_code},{new_prod_name},{new_cost},{new_quantity}''')
                print("Inventory updated successfully.\n")
                break
        except ValueError:
            print("Your input is not a number. Please try again.")


# Define 'view_all' function
#   print comprehensive list of all data contained in 'shoe_list'
def view_all():
    print("All inventory items and information:\n")
    for i in range(len(shoe_list)):
        print(f'''Product name: {shoe_list[i].product}
Product code: {shoe_list[i].code}
Country of origin: {shoe_list[i].country}
Product quantity: {shoe_list[i].quantity}
Unit cost: R {shoe_list[i].cost}.00\n''')
    print()


# Define 're_stock' function
def re_stock():
    quantities = []
    for i in range(len(shoe_list)):
        quantities.append(shoe_list[i].get_quantity())

    #obtain index of shoe object with lowest 'quantity'.
    lowest_stock = min(quantities)
    for j in range(len(shoe_list)):
        if lowest_stock == shoe_list[j].get_quantity():
            lowest_product = shoe_list[j].product
            count = j + 1

    print(f'''The following product/s has/have the lowest stock quantity:
        Product Name: \t\t\t{lowest_product}.
        No. of pairs in stock: \t{lowest_stock}.\n''')

    # read through file and store data in a list (new_data) to be manipulated.
    new_data = []
    with open("L1_caps/inventory.txt", "r") as r:
        data = r.readlines()
        for line in data:
            temp = line.strip().split(",")
            new_data.append(temp)

    # within 'while' loop, present options to user & manipulate 'new_data' accordingly. Then write data back to file.
    #   Use 'try - except' block to catch potential value errors.
    restock_option = ""
    while restock_option != 3:
        print("----------Restock Menu----------\n")
        try:
            restock_option = int(input('''What would you like to do?
    1 - Double the current stock
    2 - Specify the number of pairs to be added
    3 - Return to main menu: \n'''))
            if restock_option == 1:
                new_quantity = lowest_stock * 2
                new_data[count][-1] = str(new_quantity)
                with open("L1_caps/inventory.txt", "w") as new:
                    for row in new_data:
                        new.write(",".join([str(item) for item in row]) + "\n")
                print("Inventory updated successfully.\n")
                break

            elif restock_option == 2:
                add_quantity = int(input("Enter the number of units to add to inventory: "))
                new_quantity = lowest_stock + add_quantity
                new_data[count][-1] = str(new_quantity)
                try:
                    with open("L1_caps/inventory.txt", "w") as new:
                        for row in new_data:
                            new.write(",".join([str(item) for item in row]) + "\n")
                    print("Inventory updated successfully.\n")
                    break
                except ValueError:
                    print(f"'{add_quantity}' is not a number. Please enter the number of units to add to inventory")

            elif restock_option == 3:
                break

            elif restock_option >= 4:
                print("Enter a number between 1 and 3 to choose your desired option.")

        except ValueError:
            print("You have not entered a number. Please enter a number to choose your desired option.")


# Define 'search_shoe' function
#   obtain from user code to be searched for
#   using for loop with nested if statement, iterate through 'shoe_list' and compare 'search_code' with '"object".code'
#   if match is found print contents of object in a comprehensive manner. If not, inform user accordingly.
def search_shoe():
    search_code = input("Enter the code that belongs to the shoe you're looking for: \n")
    for i in range(len(shoe_list)):
        if search_code == shoe_list[i].code:
            print(f'''Here is the data on item code '{search_code}':
            Product name: {shoe_list[i].product}
            Product code: {shoe_list[i].code}
            Country of origin: {shoe_list[i].country}
            Product quantity: {shoe_list[i].quantity}
            Unit cost: R {shoe_list[i].cost}.00\n''')
            break
    else:
        print(f"The code you entered ({search_code}) does not exist. Try again.")


# Define 'value_per_item' function
#   Initialize empty list 'total_values_list'
#   using for loop, iterate through 'shoe_list' and multiply each object's 'cost' by its 'quantity' to get its total
#       value & append to empty list.
#   Print each object's name ("object".product) with its total value.
def value_per_item():
    total_values_list = []
    print(f'''Product Names with their respective Total Values:\n''')
    for i in range(len(shoe_list)):
        temp = shoe_list[i].get_cost() * shoe_list[i].get_quantity()
        total_values_list.append(temp)
        print(f"{shoe_list[i].product}:\t\tR{total_values_list[i]}0")
    print()


# Define 'highest_qty' function
#   Initialize empty list 'quantities' & append it with the "quantities" of each object in 'shoe_list'
#   find the maximum of 'quantities' list & compare with the "quantities" of each object in 'shoe_list'
#       to find the object with the highest 'quantity'.
def highest_qty():
    quantities = []
    for i in range(len(shoe_list)):
        quantities.append(int(shoe_list[i].quantity))


    highest_stock = max(quantities)
    for j in range(len(shoe_list)):
        if highest_stock == int(shoe_list[j].quantity):
            highest_product = shoe_list[j].product
            print(f'''The Nike {highest_product} is now on sale.''')
    print()


#==========Main Menu=============

print("Welcome to Nike World's Stock Management System!\n")
menu = ""
print()
read_shoes_data()
while menu != "e":
    print("----------Main Menu----------")
    menu = input('''Please enter your choice from the menu below:
's' - Search for a shoe model in stock by typing its product code.
'va' - View information on all the shoe models in stock.
'c' - Capture and save a new stock item to inventory.
'r' - View the item with the lowest quantity and restock that item.
'h' - View the item with the highest quantity and the current special on that item.
't' - View the total stock value for each item.
'e' - Exit. \n''').lower()
    if menu == "s":
        search_shoe()

    elif menu == "va":
        view_all()

    elif menu == "c":
        capture_shoes()

    elif menu == "r":
        re_stock()

    elif menu == "h":
        highest_qty()

    elif menu == "t":
        value_per_item()

    else:
        print("Unrecognized selection. Try again.")
