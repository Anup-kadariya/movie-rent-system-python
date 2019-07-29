import datetime
import showMovie
import update
def RentMovie():
    lst=showMovie.dict()
    a=showMovie.showMovie()
    name=input("Enter your/customer name: ")
    x=True
    while(x==True):
        try: #1
            Id=int(input("Enter movie ID:"))
            if(Id in lst):
                y=True
                while(y == True):
                    try: #2
                        quantity=int(input("How many copies of movie do you want to rent? "))
                        if(quantity<=int(lst[Id][2]) and quantity > 0):
                            price=lst[Id][1].replace("$","")
                            totalPrice=float(price)*quantity
                            break
                        else:
                            print("Input is out of stock or less than 0")
                            y=True
                    except: #2
                        print("Please give input in integer")
                break
            else:                               #when user input wrong movie ID
                print("Movie ID is incorrect!")
                x=True
        except: #1
            print("Please give input in number")




            
    #update movies and reduce quantity of movies rented
    lst[Id][2]=int(lst[Id][2])-quantity
    update.update(lst)

    #write the file of rented movies
    now=datetime.datetime.now()
    todaysDate=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    currentDateTime= datetime.datetime.now()                    
    random=(currentDateTime.minute+currentDateTime.second)                
    rentBillFileName=open("Rent-"+str(name)+str(random)+".txt","w")
    rentBillFileName.write("Rent details"+
                "\n"+"Name of person is: "+ str(name) +
                "\n"+"Date and time is: "+ str(todaysDate)+
                "\n"+"Quantity of movie: "+ str(quantity)+
                "\n"+"Total Amount is: $"+str(totalPrice)+
                "\n"+"Rented movie ID:"+ str(Id)+"\n")        

    #display details of rented movie
    print("\n\nMovie Sucessfully rented !!!")
    print("\n\t\t --recipt--")
    print("\t\t Name of person =",name)
    print("\t\t Movie Name=",lst[Id][0])
    print("\t\t No. of copies of movie =",quantity)
    print("\t\t Total Price = $",totalPrice)
    print("\t\t Date and Time of movie rent= ",todaysDate,"\n\n")
    return name,Id,quantity,totalPrice

def recipt():
    ss=RentMovie()
    value=list(ss)
    print(value)


#RentMovie()
