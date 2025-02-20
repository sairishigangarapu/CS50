answer = str(input("What is the answer to the Great Question of Life, the Universe and Everything?"))
answer1 = answer.strip(" ")
answer2 = answer1.lower()
if answer2 in ["42","forty two","forty-two"]:
    print("Yes")
else :
    print("No")
