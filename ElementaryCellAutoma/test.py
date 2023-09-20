import random
import pygame
import time
import sys


#          0     0      0        0     0    1         0     1    0         0    1     1        1    0     0         1    0     1        1    0    0         1    1    1
rules={ (False,False,False):0,(False,False,True):0,(False,True,False):0,(False,True,True):0,(True,False,False):0,(True,False,True):0,(True,True,False):0,(True,True,True):0}

#for decimal access
keys=[(False,False,False),(False,False,True),(False,True,False),(False,True,True),(True,False,False),(True,False,True),(True,True,False),(True,True,True)]
#print(rules)

   
def ruleGenerator(n):
    #binary
    i=0
    while(n//2!=0):
        bit = n%2
        rules[keys[i]]=bit
        i+=1
        n//=2

def randomSequence(size):
    randomSequence=[]
    for i in range(0,initialSize):
        randomSequence.append(random.randint(0,1))
    return randomSequence
    

def next(sequence):
    next=[]
    for i in range(1,len(sequence)-1):
        (b0,b1,b2) = (sequence[i-1],sequence[i],sequence[i+1])
        next.append(rules[(b0,b1,b2)])
    return next
      

        
ruleGenerator(255)

#print(rules)

initialSize=100
cellSize=5

nextSeq=randomSequence(initialSize)
print("initialSequence: "+str(nextSeq))


##################GRAPHICS
pygame.init()
pygame.font.init()

screenSizeX=initialSize*cellSize
screenSizeY=initialSize*cellSize

screen = pygame.display.set_mode((screenSizeX, screenSizeY), 0)
WHITE = (255,255,255)

epochCounter=0
epochTime=1000
epochIncrement=50
currentTime=0
EPOCH_TIME_MIN=50
EPOCH_TIME_MAX=1000
delay=15



cells=[]

while(True):
                
    screen.fill(0)
    
    row=0
    col=0   
    for seq in cells:
        col=row #first column
        for cell in seq:          
            if(cell==1):           
                pygame.draw.rect(screen,WHITE,(row, col, cellSize, cellSize))                 
            col+=cellSize
        row+=cellSize
    
    if(len(nextSeq)>=3):
        
        epochStart = time.time()
        if(currentTime>=epochTime):
            if(epochCounter>0):
                epochCounter+=1
            
            
            currentTime=0
            print("*** EPOCH:"+str(epochCounter)+" ***   ", end="\r")
            
               
            nextSeq=next(nextSeq)
            cells.append(nextSeq)
            
    else:
        print("FINISHED")
      
    
    #events
    for event in pygame.event.get():
    
        if(event.type == pygame.QUIT):
             pygame.display.quit()
             pygame.quit()
             sys.exit()
             
        if(event.type == pygame.KEYDOWN):
        
            if(event.key == pygame.K_KP_PLUS):
                if(epochTime >= EPOCH_TIME_MIN-epochIncrement):
                    print("\nEpochTime: "+str(epochTime))
                    epochTime -= epochIncrement
                    
            if(event.key == pygame.K_KP_MINUS):            
                if(epochTime <= EPOCH_TIME_MAX+epochIncrement):
                    print("\nEpochTime: "+str(epochTime))
                    epochTime += epochIncrement
        
        
                   
    pygame.display.update()     
    pygame.time.delay(delay)
      
    currentTime+=delay

    
        
        
        
        
        
        




        
        
        
        
        
        
