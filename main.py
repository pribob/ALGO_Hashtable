from HashTable import HashTable
import csv
from tabulate import tabulate
import json
from matplotlib import pyplot as plt
from datetime import datetime as dt


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
    # imports ALL the data of the file 'name.csv' in subfolder TestCSVData
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

def search_stock_in_hashtable(table,key):
    # if stock was added to table
    if table[key] is not None:
        # if data was imported to added stock
        if "data" in table[key]:
            # formatted output of the most recent data for specific stock
            print(tabulate([table[key]["data"][0]],headers=["Date","Open","High","Low","Close","Adj Close","Volume"]))

        else:
            print("Entry exists, but without data to show. Please use the import command.")

    else:
        print("Stock was not added yet. Please use the add command.")

    return 0

def plot_stock_curve(table,key):
    # if stock was added to table
    if table[key] is not None:
        # if data for added stock was imported
        if "data" in table[key]:
            x = []
            y = []
            dataset = table[key]["data"]
            for entry in dataset:
                x.append(dt.strptime(entry[0],'%Y-%m-%d'))
                y.append(float(entry[4]))
            plt.plot(x,y)
            plt.show()


# loads stored hashtable. json format only.
def load_hashtable_from_file(table,file):
    with open (f'./{file}.json', 'r') as file:
        data = json.load(file)
    for element in data:
        index = element["index"]
        table.array[index] = element["row"]

    print("Hashtable loaded from file.")
    return 0

# stores hashtable in a json file
def save_hashtable_to_file(table, filename):
    data = []
    with open(filename+'.json','x') as file:
        for index,element in enumerate(table.array):
            if element is not None:
                json_data = {"index":index,"row":element}
                data.append(json_data)

        json.dump(data,file,indent=6)




    print("Hashtable saved")
    return 0


if __name__ == '__main__':
    # instance of Hashtable class
    table = HashTable()
    # string for user input
    cmd_str = ""
    # filtered command of user
    cmd = ""
    # arguments for specific comment
    cmd_value = []
    while cmd != "quit":
        cmd_string = input("Enter command to run: ")
        cmd = cmd_string.split()[0]
        cmd_value = cmd_string.split()[1:]

        match cmd:

            case "add":
                # check exactly 3 arguments: shortsign= key, name of stock, number of stock WKN
                if len(cmd_value) == 3:
                    add_stock(table,cmd_value[0],{"name":cmd_value[1],"wkn":cmd_value[2]})
                else:
                    print("Wrong number of arguments: <add> <shortsign> <name> <wkn>")

            case "delete":
                delete_stock(table,cmd_value[0])
            case "import":
                import_data_of_stock(table,cmd_value[0])
            case "search":
                search_stock_in_hashtable(table,cmd_value[0])
            case "plot":
                plot_stock_curve(table,cmd_value[0])
            case "load":
                load_hashtable_from_file(table,cmd_value[0])
            case "save":
                save_hashtable_to_file(table,cmd_value[0])
            case "quit":
                break
            case "print":
                table.print()
            case _:
                print("Command not available. Please enter valid command.")











