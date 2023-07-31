num = int (input("Enter a two digit number"))
if num > 10 :
    print("Your number is larger than 10")
    if num %2 == 0 : 
        print("Your number is even")
        #% means modulo
elif num < 10 :
    print("Your number is below 10")
    if num %2 == 1 :
        print("Your number is odd")

    
        
