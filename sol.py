test = int(raw_input())

for t in range(0, test):

    N = int(raw_input())
    A = []
   
    count=0
    
    for i in range(0, N):

        numbers = raw_input()
        a, b = [int(x) for x in numbers.split(' ')]
        A.append((b,a))
        A.sort()
    
        temp=0
        inter=0
        i=0
    for x,y in A: 
        if i==0:
            count+=1
            i=1
            temp=x
        else:
            if y>inter:
                #print y,b
                count+=1
                if temp>=y:
                    inter=temp
                temp=x
                
            
        
        
    #result = 0
    
    print count
