from HashTable import HashTable
import csv

def add_stock(table,key,value):

    table.__setitem__(key,value)
    print("Stock added to hashtable")
    return 0

def delete_stock(table,key):
    table.__delete__(key)
    print("Stock deleted from hashtable")
    return 0

def import_data_of_stock(table,name):
    data = []

    if table[name]!= None:
        try:
            with open(f'./TestCSVData/{name}.csv', newline='') as test:
                reader = csv.reader(test, delimiter=',', quotechar='|')
                for index, row in enumerate(reader):
                    if index == 0:
                        continue

                    data.append(row)
            table[name]["data"]=data
            print("Imported data from stock")
        except FileNotFoundError:
            print("Sorry the file you want to import data from doesnt exist in the specified directory.")
    else:
        print("This stock you want to import data from was not added yet.")
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
                import_data_of_stock(table,cmd_value[0])
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


        #table["NN"]["data"]=data
        #print(data)
        #for element in table.array:
        #    print(element)








