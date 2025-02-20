import csv
import sys
from tabulate import tabulate

if len(sys.argv) > 2 :
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2 :
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 2 and sys.argv[1][-4:] != ".csv" :
    sys.exit("Not a CSV file")
else:
    try :
        with open(sys.argv[1]) as file:
            x = csv.reader(file)
            print(tabulate(x,headers = "firstrow",tablefmt = "grid"))
    except FileNotFoundError :
        sys.exit("File does not exist")
