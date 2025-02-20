import sys
def main():
    x = input("Enter Fuel in the form of X/Y form:")
    y = convert(x)
    z = gauge(y)
    print(z)
def convert(fraction):
    try:
        #print("The value of fraction is ",fraction)
        fraction = fraction.strip().split("/")
        #print ("Value after strip and split",fraction)
        fuel = (((int(fraction[0]))/int(fraction[1]))*100)
        return fuel
    except(ZeroDivisionError,ValueError,IndexError):
        main()
        sys.exit()
def gauge(percentage):
    if  percentage <= 1 :
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    elif percentage > 100:
        main()
        sys.exit()
    else:
        return str(round(float(percentage)))+"%"

if __name__ == "__main__":
    main()
