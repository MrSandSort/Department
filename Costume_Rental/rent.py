
import time

def getFile():
    
    fyy = open("stock.txt","r")
    data = fyy.readlines()
    fyy.close()    
    return data


def createDict(fyy):

    dataInDictionary={}

    for index in range(len(fyy)):
        
        dataInDictionary[index+1] = fyy[index].replace("\n","").split(",")

    return dataInDictionary
    


def printCostume(induce):
    
    print("----------------------------------------------------------------")
    print("ID", "\t","Costume Name", "\t", "Brand", "\t\t", "Price", "\t\t","Quantity")
    print("----------------------------------------------------------------")

    for key,value in induce.items():

        print(key, "\t", value[0], "\t", value[1], "\t$", value[2], "\t\t", value[3])
        print("-----------------------------------------------------------------")
        
    return("")

    

def getValidID(induce):
    
    
    validID = False

    while validID == False:
        
        ID = int(input("Please, Enter ID of custome you want to rent: "))

        if ID >0 and ID<=len(induce) :
            
            validID = True
            
            print("The ID of custome is ",ID)
            print()
            
            print("+++++++++++++++++++++++++++++++++++")
            
            print(" The costume is available")
            
            print("++++++++++++++++++++++++++++++++++++")
            print()

            return ID

        else:
            print("Invalid input, Please enter the valid ID")


def getValidQty(induce,ID):
    
    validQty= True

    while validQty == True:
        
        print()
        qty= int(input("Please select the quantity you want to rent: \n" ))

        if qty> 0 and qty<= int(induce[ID][3]):
            
            validQty=False
            
            induce[ID][3] = str(int(induce[ID][3]) - qty)

            return qty
        
        
        elif qty > int(induce[ID][3]):
            
            print("Quantity you want exceeds our stock quantity")
            

        else:
            print("Invalid Input, Please enter the valid input")
            

fyy = getFile()
induce = createDict(fyy)

            

def rentCostume():
    
    total_custome=[]
    total_brand=[]
    total_price=[]
    total_quantity=[]
    amount=[]
    Price=0
    Quantity=0
    Id=[]
        
    
    while True:
        
        print(printCostume(induce))
        ID=getValidID(induce)
        qty=getValidQty(induce,ID)
        print(printCostume(induce))
        
        f=open("stock.txt","w")

        value_rent= induce.values()
        

        for value in value_rent:

            string=",".join(value)
            f.write(string)
            f.write("\n")

        f.close()

        print()

        print("----------------------------")
        print("     Stock Updated          ")
        print("----------------------------")
        
        

        price=int(induce[ID][2])*int(qty)
        Price += price

        quantity=int(qty)
        Quantity +=quantity

        total_custome.append(induce[ID][0])
        total_brand.append(induce[ID][1])
        total_price.append(induce[ID][2])
        total_quantity.append(quantity)
        amount.append(price)
        
        print("\nPrice of custome rented is: $",price)   
        print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Have the customer rented another custome as well?")
        z= input("Please press 'y' if another custome has to be rented or else press any key. ")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        
        if z == 'y'.upper()or z == 'y':
            
            True

        else:
            
            first_name=input("Your First Name,Please\n")
            last_name= input("Give me your last Name(optional),\n")
            
            name=first_name+last_name
            
            rent_Id= input("Pass me your rent Id\n")
            print()
            print()
            print("__________________________________________________________________________")
            print()
            print("\t\t\tCustome Rental Department Invoice")
            print()
            print("__________________________________________________________________________")
            print("Rented By:",name,"\t","Rented On:",time.ctime())
            print("Rent_ID:",rent_Id)
            print("__________________________________________________________________________")
            print("S.No\t C.Name\t\t Brand \t\t Price\t Quantity\t Amount")
            print("__________________________________________________________________________")
            for x in range(len(total_custome)):
                print(x+1,"\t",total_custome[x],"\t",total_brand[x],"\t",total_price[x],"\t",total_quantity[x],"\t\t",amount[x])
                
            print("__________________________________________________________________________")
            print()
            print("\t\t\t Total Price:","$",Price)
            print()
            print("__________________________________________________________________________")

            file= open(f"{first_name}.txt","w")
            file.write(f"________________________________________________________________________\n")
            file.write(f"\t\t\t Custome Rental Department \n")
            file.write(f"________________________________________________________________________\n\n")
            file.write(f"Rented By:{name}\t Rented On:{time.ctime()}\n" )
            file.write(f"Rent_ID:{rent_Id}\n\n")
            file.write(f"________________________________________________________________________\n")
            file.write(f"S.No\t C.Name\t Brand\tPrice\t\t Quantity\t\t Amount\n")
            file.write("________________________________________________________________________\n")

            for i in range(len(total_custome)):
                file.write(f"{i+1}\t{total_custome[i]}\t{total_brand[i]}\t{total_price[i]}\t\t\t{total_quantity[i]}\t\t{amount[i]}\n")

            file.write("________________________________________________________________________\n\n")
            file.write(f"\t\t\t\t\t Total Price:${Price}\n\n")
            file.write("________________________________________________________________________")
            file.close()

            break

