camel = str(input("camel case :"))
camel1 =""
for i in camel:
    if i.isupper() == True:
        camel1 = camel1 + "_" + i.lower()
    else:
        camel1+=i
print(camel1)
