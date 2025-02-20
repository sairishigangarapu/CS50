def pricing():
    deno = [5,10,25]
    due = 50
    while due > 0 :
        print("Amount Due:" , due)
        if due > 0 :
            paid = int(input("paid amount:"))
            if paid in deno:
                due = due - paid
                if due > 0 :
                    print("Change Owed:",due)
                else :
                    print("Change Owed:",-due)
            else :
                print("Enter the correct denomination")
pricing()
