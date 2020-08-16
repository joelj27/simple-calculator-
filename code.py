num_1=int(input("enter the number A-"))
num_2=int(input("enter the number B-"))
print("1 - Addition\n2 - Substraction\n3 - Multiplication\n4 - Division\n5 - Floor Division\n6 - Modulo")
option = int(input("Enter one option from the above list:- "))
if option == 1:
   print(f"Addition: {num_1+ num_2}")
elif option == 2:
   print(f"Substraction: {num_1- num_2}")
elif option == 3:
   print(f"Multiplication: {num_1* num_2}")
elif option == 4:
   print(f"Division: {num_1/ num_2}")
elif option == 5:
   print(f"Floor Division: {num_1// num_2}")
elif option == 6:
   print(f"Modulo: {num_1% num_2}")