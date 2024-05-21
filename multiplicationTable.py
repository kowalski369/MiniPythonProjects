inp = int(input("Enter the number for multiplication table: "))
till = int(input("Enter the number till which you want the multiplication table :"))

for i in range(1,till+1):
    print(f"{inp} X {i} =",inp*i)