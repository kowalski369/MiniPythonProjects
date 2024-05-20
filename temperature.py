# Taking user input for choosing conversion of one unit to another

unitconv = input("~~~~~~~~~~~~~~From which unit to which you want to convert temperature into:~~~~~~~~~~~~~~\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n3. Celsius to Kelvin\n4. Kelvin to Celsius\n5. Fahrenheit to Kelvin\n6. Kelvin to Fahrenheit\n: ")


if unitconv == "1" :
    c = int(input("Enter the Degree Celsius temperature :"))
    f = c/5 * 9 +32 
    val = f"{c} Degree Celsius in Degree Fahrenheit is : {f} Degree Fahrenheit"
    print(val.title().center(50,"-"))
    
elif unitconv == "3" :
    c = int(input("Enter the Degree Celsius temperature :"))
    k =  c/5 * 5 +273
    print(f"{c} degree Celsius in Kelvin is : {k} Kelvin")

elif unitconv == "2" :
    f = int(input("Enter the Degree Fahrenheit temperature :"))
    c =  ((f-32)/9)*5
    print(f"{f} degree farenheit in Degree Celsius is : {c} Degree Celsius")

elif unitconv == "4" :
    k = int(input("Enter the Kelvin temperature :"))
    c = k-273/5 * 5 
    print(f"{k} Kelvin in Degree Celsius is : {c} Degree Celsius")

elif unitconv == "5" :
    f = int(input("Enter the Fahrenheit temperature :"))
    k =  5/9 *(f-32) +273
    print(f"{f} Degree Fahrenheit in Kelvin is : {k} Kelvin")

elif unitconv == "6" :
    k = int(input("Enter the Kelvin temperature :"))
    f = (k-273)/5 * 9 +32
    print(f"{k} Kelvin in Degree Fahrenheit is : {f} Degree Fahrenheit")

else:
    print("What the heck")