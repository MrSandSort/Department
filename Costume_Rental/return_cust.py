import rent,time

def file():

    first_name=input("Your Name Please!\n")

    try:
        f=open(f"{first_name}.txt","r")
        f.close()
        print("Bill exists with this name!")
        print()
        print("--------------------------------")
        print("Lets proceed further dude")
        print("--------------------------------")
        print()

    except:
        print("Bill with this name is not found!\n")
        file()

    return first_name   
        
def mis_cost():

    first_name=file()
    
    f= open("stock.txt","r")
    data= f.readlines()
    lust=[]
    
    for i in data:
        lust.append(i.strip())
    f.close()

    ft=open("stock.txt","w")

    for x in lust:
        ft.write(x)
        ft.write("\n")
    ft.close()

    rett= rent.getFile()
    dictt= rent.createDict(rett)
        
    rent.printCostume(dictt)
    
    def get_Id(dictt):
        
        validID = True

        while validID == True:

            ID = int(input("Please, Enter ID of custome you want to return: "))

            if ID >0 and ID<=len(dictt):
                validID = False
                return ID
        
            else:
                print("Invalid input, Please enter the valid ID")
                
    def get_qt(dictt,ID):

        validQty= True
        
        while validQty == True:
            print()
            qty= int(input("Select the quantity you want to return: " ))
            print()

            if qty > 0:
                validQty=False
                dictt[ID][3]=str(int(dictt[ID][3])+qty)
                return qty
            else:
                print("Quantity isn't measurable!")

    cust=[]
    bnd=[]
    pr=[]
    qt=[]
    amt=[]
    Pr=0
    Qty=0

    net=True
    
    while True:
        
        ID= get_Id(dictt)
        qty=get_qt(dictt,ID)
        rent.printCostume(dictt)
        
        f=open("stock.txt","w")
        value_return= dictt.values()
        for value in value_return:
            string=",".join(value)
            f.write(string)
            f.write("\n")
        f.close()
        
        print("---------------------------------------")
        print("\tStock Updated                        ")
        print("---------------------------------------")

        print()

        price=int(dictt[ID][2])*int(qty)
        Pr+=price

        qnty=int(qty)
        Qty += qnty

        

        cust.append(dictt[ID][0])
        bnd.append(dictt[ID][1])
        pr.append(dictt[ID][2])
        qt.append(qty)
        amt.append(price)

        ask=input("Do you want to return another custome as well?\n")
        print()

        if ask =="y".upper() or ask=="y":
            True
        else:
            days= int(input("How many days of renting has it been?\n"))
            
            if days > 5:
                fine_per_day=2
                exceed_days= days-5
                total_fine = exceed_days * fine_per_day* Qty
            else:
                exceed_days=0
                total_fine=0
                print("You're not charged any fine.\n")
                print("Thanks for returning the costume on time.")
    
            print("_________________________________________________________________________")
            print()
            print("\t      Return Invoice of Rental Department               ")
            print()
            print("_________________________________________________________________________")
            print(f"Returned by:{first_name}\t")
            print(f"Returned on:{time.ctime()}")
            print(f"Returned exceeding {exceed_days} days")
            print("_________________________________________________________________________")
            print("S.No\tCostumeName\tC.Brand\t\tPrice\tQuantity\tAmount")
            print("_________________________________________________________________________")
            for i in range(len(cust)):
                print(i+1,"\t",cust[i],"\t",bnd[i],"\t",pr[i],"\t",qt[i],"\t\t",amt[i])
            
            print()
            print("_________________________________________________________________________")
            print(f"\t TotalFine:${total_fine}\t TotalPrice:${Pr}")
            print("_________________________________________________________________________")
            print(f"\tRenting Services available for only 5 days.\n\tIf exceed,charges will be taken.")
            print("_________________________________________________________________________")

            ft= open(f"return_{first_name}.txt","w")
            ft.write(f"________________________________________________________________________\n")
            ft.write(f"\t\t\t Custome Rental Department \n")
            ft.write(f"________________________________________________________________________\n\n")
            ft.write(f"Returned By:{first_name}\t Returned On:{time.ctime()}\n"                           )
            ft.write(f"________________________________________________________________________\n")
            ft.write(f"S.No\t C.Name\t Brand\tPrice\t\t Quantity\t\t Amount\n")
            ft.write("________________________________________________________________________\n")

            for i in range(len(cust)):
                ft.write(f"{i+1}\t{cust[i]}\t{bnd[i]}\t{pr[i]}\t\t\t{qt[i]}\t\t{amt[i]}\n")

            ft.write("________________________________________________________________________\n\n")
            ft.write(f"\t TotalFine:${total_fine}\tTotal Price:${Pr}\n\n")
            ft.write("________________________________________________________________________")
            ft.close()

            break
           
        
        
    

