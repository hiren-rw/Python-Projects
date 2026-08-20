print("Welcome to the Pattern Generator and Number Analyzer!")
while True:

    print("\nSelect an option : ")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    ch = input("\nEnter Your Choice : ")

    match ch:
        case "1":
            n = int(input("Enter the number of rows for the pattern : "))
            print("\nPattern : ")

            for i in range(1,n+1):
                for j in range(i):
                    print("*",end=" ")
                print()

        case "2":
            strt = int(input("\nEnter the Start of the range : "))
            end = int(input("Enter the end of the range : "))
            total = 0

            for k in range(strt,end+1):
                if(k%2==0):
                    print("Number",k,"is Even")
                    total += k
                else:
                    print("Number",k,"is Odd")
                    total += k

            print("Sum of all Numbers from",strt,"to",end,"is : ",total)
                
        case "3":
            print("Exiting the program. Goodbye!..")
            break

        case _:
            print("Invalid")
