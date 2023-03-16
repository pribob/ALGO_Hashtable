from HashTable import HashTable

def add_stock(table,key,value):

    table.__setitem__(key,value)
    print("Stock added to hashtable")
    return 0

def delete_stock(table,key):
    table.__delete__(key)
    print("Stock deleted from hashtable")
    return 0

def import_data_of_stock():
    print("Imported data from stock")
    return 0

def search_stock_in_hashtable():
    print("Stock searched in hashtable")
    return 0

def plot_stock_curve():
    print("Plotted last 30 days of ")

def load_hashtable_from_file():
    print("Hashtable loaded from file.")
    return 0

def save_hashtable_to_file():
    print("Hashtable saved")
    return 0


if __name__ == '__main__':

    table = HashTable()

    cmd_str = ""
    cmd = ""
    #cmd_list = []
    cmd_value = []
    while cmd != "quit":
        cmd_string = input("Enter command to run: ")
        cmd = cmd_string.split()[0]
        cmd_value = cmd_string.split()[1:]

        match cmd:

            case "add":
                # check exactly 3 arguments: shortsign= key, name of stock, number of stock WKN
                add_stock(table,cmd_value[0],{"name":cmd_value[1],"wkn":cmd_value[2]})
                for element in table.array:
                    print(element)

            case "delete":
                delete_stock(table,cmd_value[0])
            case "import":
                import_data_of_stock()
            case "search":
                search_stock_in_hashtable()
            case "plot":
                plot_stock_curve()
            case "load":
                load_hashtable_from_file()
            case "save":
                save_hashtable_to_file()
            case "quit":
                break
            case _:
                print(f"Command: {cmd} \n Argument: {cmd_value}")






