
#for loop
str1="learpythonprogramming"   
index = 0
for each in str1: 
    print(index, each)
    index += 1
    
     
    
#break statement
    
list1=[10,20,30,40,50,30,50,60]
sum1=0 
for each in list1:  
    if sum1 >= 110:  
         break 
    sum1=sum1+each 
print("Sum is",sum1)