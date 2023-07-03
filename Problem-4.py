#inputs
a = [1,2,3,4,5,6,7,8,9] 
#Map function
b = map(int,input().split())
#Converting to list
b = list(b)
#Dict c Initialization 
c = {} 
#For loop
for i in a:
    #count variable initialization
    count = 0
    #for loop
    for j in b:
        #if loop
        if(j%i)==0:
            count=count+1
        else:
            #pass the case
            pass
        #update the dict c
        c.update({i:count})
print(c)