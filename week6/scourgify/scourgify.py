import csv
import sys

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) == 2 and (sys.argv[1][-4:] != ".csv" or sys.argv[2][-4:] != ".csv"):
    sys.exit("Not a csv file")
else:
    try:
        with open(sys.argv[1],"r") as file1 :
            x = csv.Dictreader(file1)
        with open(sys.argv[2],"w") as file2:
            header = ["first","last","house"]
            write = csv.Dictwriter(file2,fieldnames = header)
            csv.writeheader()
            for student in x:
                last, first = student["name"].split(", ")
                house = student["house"]
                write.writerow({"first": first, "last": last, "house": house})

    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")
