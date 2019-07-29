import datetime
import showMovie
import update
def returnMovie():
    lst=showMovie.dict()
    name=input("Enter your name: ")
    correctMovieID=True
    while(correctMovieID==True):
        try: #1
            movieID=int(input("Enter movie ID:"))
            if(movieID in lst):
                q=True
                while(q == True):
                    try: #2
                        quantity=int(input("How many copies of movie do you want to return? "))
                        if(quantity<=int(lst[movieID][2])and quantity > 0):
                            price=lst[movieID][1].replace("$","")
                            totalPrice=float(price)*quantity
                            break
                        else:
                            print("Input is out of stock or less than 0")
                            q=True 
                    except: #2
                        print("Please give input in number")
                break
            else:                               #when user input wrong movie ID
                print("Movie ID is incorrect!")
                correctMovieID=True
        except: #1
            print("Please give input in number")

    #calculating fine
    f=True
    while(f==True):
        try:    #3
            RentDays=int(input("How long have you rented this movie? -> "))
            if(RentDays>10):
                FineForDays=RentDays-10
                F=FineForDays*0.20*quantity
                fine=str("$"+str(F))
                print("\nYou have to pay "+fine+" as fine!!\n")
                break
            else:
                fine="0"
                print("\nYou do not have to pay fine!!\n")
                f=False
        except: #3
            print("Please give input in number")


    
            
#update movies and add quantity of movies returned
    lst[movieID][2]=int(lst[movieID][2])+quantity
    update.update(lst)

    
#write the file of return movies    
    now=datetime.datetime.now()
    todaysDate=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    currentDateTime= datetime.datetime.now()                    
    random=(currentDateTime.minute+currentDateTime.second)
    returnBillFileName=open("Return-"+str(name)+str(random)+".txt","w")
    returnBillFileName.write("Return slip"+
            "\n"+"Name of person is: "+ str(name)+
            "\n"+"Date and time is: "+ str(todaysDate)+
            "\n"+"Quantity of movie: "+ str(quantity)+
            "\n"+"Total Fine is: "+ str(fine)+
            "\n"+ "Returned movie ID :"+ str(movieID)+"\n")

    #display details of returned movie
    print("\n\nMovie returned Sucessfully !!!")
    print("\n\t\t --recipt--")
    print("\t\t Name of person =",name)
    print("\t\t Movie Name =",lst[movieID][0])
    print("\t\t No. of copies of movie =",quantity)
    print("\t\t Total fine = ",fine)
    print("\t\t Date and Time of movie rent = ",todaysDate,"\n\n")                
#returnMovie()
