print("Welcome to the Interactive Personal Data Collector!\n")

name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))
height = float(input("Enter Your Height in Meters : "))
num = int(input("Enter Your Favourite Number : "))

print("\nThank You! Here is the information we Collected : \n")

print("Name : ",name,"(Type : ",type(name),", Memory Address : ",id(name),")")
print("Age : ",age,"(Type : ",type(age),", Memory Address : ",id(age),")")
print("Height : ",height,"(Type : ",type(height),", Memory Address : ",id(height),")")
print("Favourite Number : ",num,"(Type : ",type(num),", Memory Address : ",id(num),")")

birth = 2026 - age
print("\nYour Birth year is : ",birth,"(Based on your age of ",age,")")

print("\nThank You for using the Personal Data Collector. Goodbye!")
