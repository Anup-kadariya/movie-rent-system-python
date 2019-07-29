def update(lst):
    file1= open("movielist.txt", "w")
    for values in lst.values():
        file1.write(str(values[0])+","+str(values[1])+","+str(values[2]))
        file1.write("\n")
    file1.close()
