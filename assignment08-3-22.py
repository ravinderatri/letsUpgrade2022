
list1=[]   
fr=open("sample.txt","r")  
index=0
for each in fr:
    if each in list1: 
        print("Duplicate line",index)
    else:
        list1.append(each) 
        index += 1 
fr.close()