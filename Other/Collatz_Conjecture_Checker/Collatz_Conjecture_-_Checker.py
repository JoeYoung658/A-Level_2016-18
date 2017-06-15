import sys 


snumb=3358
while True:
    snumb=snumb+1
    #print ("Now attempting number:", snumb)
    numb=snumb
    counter = 0
    numbs=[]
    while numb != 1:
        if numb in numbs:
            print ("SEQUENCE DOES NOT TERMINATE.")
            sys.exit()
        elif numb%2==0:
            numbs.append(numb)
            numb=numb//2
            counter+=1
        else:
            numbs.append(numb)
            numb=(3*numb)+1
            counter+= + 1
    
    file = open ("Log.txt", "a")
    file.write("Terminated - " + str(counter) + " Number - " + str(snumb))
    file.write("\n")
    file.close

   
