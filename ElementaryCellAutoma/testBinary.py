



def ruleGenerator(n):
    #binary
    i=0
    while(n!=0):
            bit = n%2
            print(str(bit),end=" ")
            i+=1
            n//=2
        
      
for n in range(0,255):
    print(str(n)+"=" , end = "") 
    ruleGenerator(n)
    print() 
        

        