import sys
import showMovie
import rentMovie
import returnMovie
def MainMenu():
    
    print("\n----------------------------------------------------------------------")
    print("---Welcome to Movie rental program---")
    print(" 1.Show movie list")
    print(" 2.Borrow movie")
    print(" 3.Return Movie")
    print(" 4.Exit")
    print("-----------------------------------------------------------------------\n")

    m=input("Enter your choice:")
    if m=='1':
        showMovie.showMovie()
        MainMenu()
    elif m=='2':
        rentMovie.RentMovie()
        #rentMovie.recipt()
        MainMenu()
    elif m=='3':
        returnMovie.returnMovie()
        MainMenu()
    elif m=='4':
        sys.exit()
    else:
        print("Wrong input")
        MainMenu()
        
MainMenu()
#recipt()
