File = open("unsorted.txt","r")
Tab = [] 
for x in File:
    try:
        Tab.append(int(x))
    except:
        print("There are incorrect values in the file --> "+str(x))
Tab.sort()
File.close()
File = open("sorted.txt","w")
for x in Tab:
    File.write(str(x)+"\n")
File.close()