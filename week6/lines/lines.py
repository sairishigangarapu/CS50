import sys
if len(sys.argv) > 2 :
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2 :
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 2 and sys.argv[1][-3:] != ".py" :
    sys.exit("Not a Python file")
else:
    try :
        x = open(sys.argv[1],"r")
        y = 0
        lines = x.readlines()
        for i in lines:
            if i.lstrip().startswith("#") or i.strip() == "":
                pass
            else:
                y+=1
        print(y)
    except FileNotFoundError:
        sys.exit("File does not exist")
