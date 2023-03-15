from HashTable import HashTable

def add_stock():
    print("Stock added to hashtable")
    return 0

def delete_stock():
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

    cmd = "quit"
    while cmd != "quit":
        cmd = input("Enter command to run: ")
        #TO-DO: add splicing -> command and arguments...
        match cmd:

            case "add":
                add_stock()
            case "delete":
                delete_stock()
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
                print("Command not supporter. Please try again")






