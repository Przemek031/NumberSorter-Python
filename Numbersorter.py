File = open("unsorted.txt","r")
Tab = [] 
for x in File:
    Tab.append(int(x))
Tab.sort()
File.close()
File = open("sorted.txt","w")
for x in Tab:
    File.write(str(x)+"\n")
File.close()