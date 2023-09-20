import random
import pygame
import time
import sys


rules={ (0,0,0):0, (0,0,1):0 ,(0,1,0):0, (0,1,1):0, (1,0,0):0, (1,0,1):0, (1,1,0):0,(1,1,1):0}

#for decimal access
keys=[(0,0,0), (0,0,1) ,(0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0),(1,1,1)]
#print(rules)

   
def ruleGenerator(n):
    #binary
    i=0
    while(n!=0):
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
        #print(str((b0,b1,b2)), end="=")
        next.append(rules[(b0,b1,b2)])
        #print(rules[(b0,b1,b2)])
        
    return next
      

      
      
#############################SIZE
initialSize=500   #100
cellSize=2   


 
##################GRAPHICS
pygame.init()
pygame.font.init()

screenSizeX=initialSize*cellSize
screenSizeY=initialSize*cellSize

screen = pygame.display.set_mode((screenSizeX, screenSizeY), 0)
WHITE = (255,255,255)
BLACK = (0,0,0)

epochCounter=0
epochTime=1000
epochIncrement=50
currentTime=0
EPOCH_TIME_MIN=50
EPOCH_TIME_MAX=1000
delay=15

#FONTSIZE = 50
#font = pygame.font.SysFont('Comic Sans MS', FONTSIZE)

##############################



initialRandom=randomSequence(initialSize)
cells=[]
colors=[]

for ruleN in range(0,256):  #################GENERATE FOR EVERY RULE
    screen.fill(WHITE)

    #print("**RULE N."+str(ruleN), end="")
    """
    ruleText = font.render(
            "RULE N." + str(ruleN), False, (0, 0, 0))
            
    w,h = font.size("RULE N." + str(ruleN))
    """
    #screen.blit(ruleText, (screenSizeX//2-w//2, screenSizeY//2-h//2))
    #pygame.display.update()  
    #pygame.time.delay(500)
     
    for key in rules.keys():
        rules[key]=0
     
    ruleGenerator(ruleN)
    finished=False
    nextSeq=initialRandom
    cells.append(initialRandom)
    
    FONTSIZE = initialSize*cellSize//10
    
    colors.append((random.randint(1,255),random.randint(1,255),random.randint(1,255)))
    c=0

    while(not finished):  ###SINGLE RULE LOOP
        screen.fill(WHITE)
        
        if(FONTSIZE>5):
            FONTSIZE-=1
            font = pygame.font.SysFont('Comic Sans MS', FONTSIZE)
            
            
            ruleText = font.render(
            "RULE N." + str(ruleN), False, (0, 0, 0))
                
            w,h = font.size("RULE N." + str(ruleN))
            
            #screen.blit(ruleText, (screenSizeX//2-w//2 - len(cells), screenSizeY//2-h//2 - len(cells)))   ##LOLOL
            screen.blit(ruleText, (screenSizeX//2-w//2 , screenSizeY//2-h//2 ))
        
        
        row=0
        col=0   
        for seq in cells:
            col=row #first column
            for cell in seq:          
                if(cell==1):           
                    pygame.draw.rect(screen,colors[c],(col, row, cellSize, cellSize))
                    pygame.draw.rect(screen,colors[c],(row, col, cellSize, cellSize))
                    pygame.draw.rect(screen,colors[c],(screenSizeX-col, screenSizeY-row, cellSize, cellSize))
                    pygame.draw.rect(screen,colors[c],(screenSizeX-row, screenSizeY-col, cellSize, cellSize))                
                col+=cellSize
            row+=cellSize
        
        if(len(nextSeq)>=3):
                              
                nextSeq=next(nextSeq)
                cells.append(nextSeq)
                colors.append((random.randint(1,255),random.randint(1,255),random.randint(1,255)))
                c+=1
                
        else:
            #print("  -> FINISHED**", end="\r")
            finished=True
            cells.clear()
            colors.clear()   ###or use same colors?
            pygame.time.delay(1000)
          
        
        #events
        for event in pygame.event.get():
        
            if(event.type == pygame.QUIT):
                 pygame.display.quit()
                 pygame.quit()
                 sys.exit()
                 
            if(event.type == pygame.KEYDOWN):
            
                if(event.key == pygame.K_KP_PLUS):
                    if(epochTime >= EPOCH_TIME_MIN-epochIncrement):
                        #print("\nEpochTime: "+str(epochTime))
                        epochTime -= epochIncrement
                        
                if(event.key == pygame.K_KP_MINUS):            
                    if(epochTime <= EPOCH_TIME_MAX+epochIncrement):
                        print("\nEpochTime: "+str(epochTime))
                        #epochTime += epochIncrement
            
            
                       
        pygame.display.update()     
        pygame.time.delay(delay)
          
        #currentTime+=delay

      