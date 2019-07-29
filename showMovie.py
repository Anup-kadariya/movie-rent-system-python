#It will read and display the movie detials saved on file
def showMovie():
    print("----------------------------------------------------------------------")
    print ("Movie ID        Movie-Name", "\t\t", "Price", "\t\t", "Quantity")
    print("----------------------------------------------------------------------")
    file=open("movielist.txt","r")
    MI=1
    for line in file:
        print("  ",MI,"\t\t"+line.replace(",","\t\t "))
        MI=MI+1
    print("----------------------------------------------------------------------")
    #return showMovie()
def dict():
    file1=open("movielist.txt","r")
    d={}
    s=1
    for line in file1:
        line=line.replace("\n","")
        d[s]= line.split(",")
        s=s+1
    return d 
#dict()

