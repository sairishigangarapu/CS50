def main():
    text = input("Input: ")
    output = shorten(text)
    print(f"Output: {output}")

def shorten(y):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    word =""
    for i in y:
        if i not in vowels:
            word += i
    return word
if __name__ == "__main__":
    main()
