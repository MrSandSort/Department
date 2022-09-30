

import rent as rent,return_cust

print()
print("WELCOME TO COSTUME RENTAL APPLICATION")

option='''

Select desirable option
(1) || Press 1 to rent a custome.
(2) || Press 2 to return a custome.
(3) || Press 3 to exit

'''


def displayMessage():
    
    """ Inside the function, a while loop is continously executes until the user wants to exit"""
    
    while True:
        
        print(option)

        try:
            choose =int(input("Choose an Option "))
            print()

            if(choose == 1):
                print("++++++++++++++++++++++++++++++")
                print("Lets Rent a Costume.")
                print("++++++++++++++++++++++++++++++\n")
                rent.rentCostume()
            
            elif(choose== 2):
                print("++++++++++++++++++++++++++++++")
                print("Lets return a custome")
                print("++++++++++++++++++++++++++++++\n")
                return_cust.mis_cost()
                
            elif(choose == 3):
                print()
                print(" Thank you for using our application")
                print()
                exit()
                
            else:
                print("Invalid input!!!")
                print("Please select the value as per the provided options")
                print()
        except:
            print("This format is not allowed to attempt....")
            print("Try Again!!")
       
        
            
displayMessage()





