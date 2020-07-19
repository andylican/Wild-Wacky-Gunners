#--------------------------------------------------------------------------------------------#
#Andy Li and Matthew Sekirin
#Jan 18, 2018
#wildWackyGunnersFinal.py
#Creates a player vs. player shooting game that ends when one of the characters loses 5 lives
#---------------------------------------------------------------------------------------------#

#initialize program 
import pygame
import random
import math
pygame.init()
HEIGHT = 700
WIDTH = 1300
halfHEIGHT = HEIGHT / 2
halfWIDTH = WIDTH / 2
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#load images and initialize lists
coltPic = [0] * 8
coltPic2 = [0] * 8
nextColt = [0,1,2,3,4,5,6,7]
nextColt2 = [0,1,2,3,4,5,6,7]
barrier = [1,1,1,1,1,1,1,1]
colt = pygame.image.load("colt2-1 - Copy2.png")
coltPic[0] = pygame.image.load("colt0-1 - Copy2.png")
colt2 = pygame.image.load("colt2-2 - Copy2.png")
background = pygame.image.load("sandUpdated.jpg").convert()
cactus = pygame.image.load("cactus.png").convert_alpha()
well = pygame.image.load("well.png")
tent = pygame.image.load("tent.png")
tent2 = pygame.image.load("tent2.png")
badge = pygame.image.load("sheriffBadge.png")
badge2 = pygame.image.load("sheriffBadge2.png")
gunsMain = pygame.image.load("guns.png")
coltPortrait = pygame.image.load("Colt_Portrait.png")

for i in range(1,8):
    coltPic[i] = pygame.image.load("colt" + str(i) + "-1 - Copy2.png")
for k in range(8):
    coltPic2[k] = pygame.image.load("colt" + str(k) + "-2 - Copy2.png")


#define colours
BLACK = (0, 0, 0)
BLACK_SECOND = (32,32,32)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
RED_BLOOD = (138,7,7)
RED_COPPER = (146,21,18)
GREEN = (0,223,56)
BROWN = (150, 100, 50)
BLUE_DARK = (0,0,64)

#define fonts
font = pygame.font.SysFont("Pacifico", 80)
font2 = pygame.font.SysFont("Times New Roman", 30)
font3 = pygame.font.SysFont("Times New Roman", 18,0,1)
font4 = pygame.font.SysFont("Playbill",30)
font5 = pygame.font.SysFont("Times New Roman",21,1,1)
font6 = pygame.font.SysFont("Pacifico",50)


wait = 12
inPlay = True

#player 1 variables
p1W = coltPic[0].get_width()
p1H = coltPic[0].get_height()
p1X = random.randint(20,100)
p1Y = random.randint(16,HEIGHT - p1H)
badgeW = badge.get_width()

p1Speed = 3
coltNum = 2
coltNumNew = 2
direction = ""
password = True
p1Health = 50
bullX = []
bullY = []
bullR = 5
bullSpeed = 15
bullDis = []
bullDir = []
bullScreen = []
rocX = []
rocY = []
rocR = 10
rocSpeed = 10
rocDis = []
rocDir = []
rocScreen = []
status = "ok"
weapon = "Rocket"
explosion = False
expX = -300
expY = -300
expR = 100
expDmg = True
expDmgS = True

#player 2 variables
p2W = colt2.get_width()
p2H = colt2.get_height()
p2X = random.randint(WIDTH - 100 - p1W, WIDTH - 20 - p1W )
p2Y = random.randint(16,HEIGHT - p1H)

p2Speed = 3
coltNum2 = 2
coltNumNew2 = 2
direction2 = ""
password2 = True
p2Health = 50
bullX2 = []
bullY2 = []
bullR2 = 5
bullSpeed2 = 15
bullDis2 = []
bullDir2 = []
bullScreen2 = []
rocX2 = []
rocY2 = []
rocR2 = 10
rocSpeed2 = 10
rocDis2 = []
rocDir2 = []
rocScreen2 = []
status2 = "ok"
weapon2 = "Rocket"
explosion2 = False
expX2 = -300
expY2 = -300
expR2 = 100
expDmg2 = True
expDmgS2 = True


#graphics-related variables
stop = 0
backX = 0
backY = 0
backW = 3000
backH = 1997
cactusX = 300
cactusY = 300
cactusW = cactus.get_width()
cactusH = cactus.get_height()
wellW = well.get_width()
wellR = wellW / 2
wellX = halfWIDTH - wellR
wellY = 400
wellCenterY = 400 + wellR
tentW = tent.get_width()
tentX = 400
tentY = 200
tentR = tentW / 2
tentX2 = halfWIDTH + 250 - tentW
tentCenterY = tentY + tentR + 30
tentCenterX = tentX + tentR
tentCenterX2 = tentX2 + tentR
cactusXList = []
cactusYList = []
boulderY = -100
gunsMainW = gunsMain.get_width()
coltPortraitW = coltPortrait.get_width()


#health and damage variables
timeNow = 0
lives = 5
lives2 = 5
timeNow2 = 0
healthChange = 0
healthChange2 = 0
damageTime = 0
damageTime2 = 0
damageTimeNew = 0
damageTimeNew2 = 0
dangerCactus = 0
dangerCactus2 = 0
cactCount = 0
cactCount2 = 0
healthCount = 0
healthCount2 = 0
helpHealth = 0
helpHealth2 = 0


#booleans
inPlayMain = True
play = False
instruct = False
back = False
liveLoss = False
liveLoss2 = False
p1Win = False
p2Win = False
gameOver = False
loserBlit = True
healing = False
healing2 = False

#initialize raw cactus image positions
for h in range(10):
    cactusX = random.randint(0,300)
    cactusXList.append(cactusX)
    cactusX = random.randint(1000,WIDTH - cactusW)
    cactusXList.append(cactusX)
    for i in range(2):
        cactusY = random.randint(0,HEIGHT - cactusH)
        cactusYList.append(cactusY)

#update positions so that no two pictures are overlapping
for j in range(20): #for each cactus
    stop = 0
    while stop != 20:
        for k in range(0,20):
            if j != k:
                if abs(cactusXList[j] - cactusXList[k]) < cactusW and abs(cactusYList[j] - cactusYList[k]) < cactusH:
                    if cactusXList[j] <= 300:
                        cactusXList[j] = random.randint(0,300)
                        stop = 0
                        break
                    else:
                        cactusXList[j] = random.randint(1000,WIDTH - cactusW)
                        stop = 0
                        break
                    cactusYList[j] = 0,HEIGHT - cactusH
                else:
                    stop += 1
                if stop == 20:
                    break
healthBarX = p1X - (50 - p1W) / 2
healthBarX2 = p2X - (50 - p2W) / 2


#-------------------------#
#functions start here
#-------------------------#
def distance(x1, x2, y1, y2):
    dis = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return dis

def redrawScreen():
    global timeNow
    global cactus
    global stop
    global p1X
    global p1Y
    global p2X
    global p2Y
    global p1Health
    global p2Health
    global lives
    global lives2
    global cactCount
    global cactCount2
    global healthCount
    global healthCount2
    global damageTimeNew
    global damageTimeNew2
    global healthChange
    global healthChange2
    global healthCactChange
    global healthCactChange2
    global liveLoss
    global liveLoss2
    global healthBarX
    global healthBarX2
    global helpHealth
    global helpHealth2
    global healing
    global healing2

    screen.blit(background, (backX, backY)) #blit background picture
    
    #draw obstacles
    screen.blit(tent,(tentX,tentY))
    screen.blit(tent2,(tentX2,tentY))
    for h in range(20):
        screen.blit(cactus,(cactusXList[h],cactusYList[h]))
    screen.blit(well,(wellX, wellY))

    #turning animations
    global password
    global password2
    rand = random.randint(0,1)
    if coltNum - coltNumNew < 0 and password:
        if coltNum - coltNumNew < -4 or (coltNum - coltNumNew == -4 and rand):
            for h in range(0,8):
                if h > coltNumNew or (h <= coltNum and h > 0):
                    nextColt[h] -= 1
                if h == 0:
                    nextColt[h] = 7
        else:
            for h in range(coltNum,coltNumNew):
                nextColt[h] += 1
    if coltNum - coltNumNew > 0 and password:
        if coltNum - coltNumNew > 4 or (coltNum - coltNumNew == 4 and rand):
            for h in range(0,8):
                if h < coltNumNew or (h >= coltNum and h < 7):
                    nextColt[h] += 1
                if h == 7:
                    nextColt[h] = 0
        else:         
            for h in range(coltNum,coltNumNew,-1):
                nextColt[h] -= 1
    password = False
    rand2 = random.randint(0,1)
    if coltNum2 - coltNumNew2 < 0 and password2:
        if coltNum2 - coltNumNew2 < -4 or (coltNum2 - coltNumNew2 == -4 and rand2):
            for h in range(0,8):
                if h > coltNumNew2 or (h <= coltNum2 and h > 0):
                    nextColt2[h] -= 1
                if h == 0:
                    nextColt2[h] = 7
        else:
            for h in range(coltNum2,coltNumNew2):
                nextColt2[h] += 1
    if coltNum2 - coltNumNew2 > 0 and password2:
        if coltNum2 - coltNumNew2 > 4 or (coltNum2 - coltNumNew2 == 4 and rand2):
            for h in range(0,8):
                if h < coltNumNew2 or (h >= coltNum2 and h < 7):
                    nextColt2[h] += 1
                if h == 7:
                    nextColt2[h] = 0
        else:         
            for h in range(coltNum2,coltNumNew2,-1):
                nextColt2[h] -= 1

    #course of action after a loss of a life
    if p1Health <= 0:
        lives -= 1
        liveLoss = True
        p1Health = 50
        p1X = random.randint(20,100)
        p1Y = random.randint(16,HEIGHT - p1H)  
    if p2Health <= 0:
        lives2 -= 1
        liveLoss2 = True
        p2Health = 50
        p2X = random.randint(WIDTH - 100 - p1W, WIDTH - 20 - p1W )
        p2Y = random.randint(16,HEIGHT - p1H)

    #draw players
    screen.blit(coltPic[coltNum], (p1X, p1Y))
    screen.blit(coltPic2[coltNum2], (p2X, p2Y))
    password2 = False
    
    #drawing weapons
    if weapon == "Pistol" and not(healing):
        for i in range(len(bullX)):
            if bullScreen[i]:
                pygame.draw.circle(screen, RED, (bullX[i], bullY[i]),bullR)
    if weapon == "Rocket" and not(healing):
        for i in range(len(rocX)):
            if rocScreen[i]:
                pygame.draw.circle(screen, BLACK, (rocX[i], rocY[i]), rocR)
    if weapon2 == "Pistol":
        for i in range(len(bullX2)):
            if bullScreen2[i]:
                pygame.draw.circle(screen, RED, (bullX2[i], bullY2[i]),bullR2)
    if weapon2 == "Rocket":
        for i in range(len(rocX2)):
            if rocScreen2[i]:
                pygame.draw.circle(screen, BLACK, (rocX2[i], rocY2[i]), rocR2)
    if explosion:
        pygame.draw.circle(screen, RED, (expX, expY), 100)
    if explosion2:
        pygame.draw.circle(screen, RED, (expX2, expY2), expR)
        

    #damage from cactuses and damage shown on health bars

    #edited after submission
    healthCactChange = 5
    healthCactChange2 = 5

    timeNow = pygame.time.get_ticks()
    if (timeNow - damageTimeCactus) / 1000 == cactCount:
        cactCount += 1
        damageTimeNew = pygame.time.get_ticks()
        p1Health -= 5
        healthCactChange = 5
        healthChange = 5
    if (timeNow - damageTimeCactus2) / 1000 == cactCount2:
        cactCount2 += 1
        damageTimeNew2 = pygame.time.get_ticks()
        p2Health -= 5
        healthCactChange2 = 5
        healthChange2 = 5
    if liveLoss:
        damageTimeNew = 0
    if liveLoss2:
        damageTimeNew2 = 0
    liveLoss = False
    liveLoss2 = False
    elapsed = timeNow - damageTime
    elapsed2 = timeNow - damageTime2
    elapsedNew = timeNow - damageTimeNew
    elapsedNew2 = timeNow - damageTimeNew2
    if elapsed < 200 or elapsedNew < 200:
        pygame.draw.rect(screen, RED_BLOOD, (healthBarX + p1Health, p1Y - 15, healthChange, 10))
        pygame.draw.rect(screen, RED_BLOOD, (healthBarX + p1Health, p1Y - 15, healthCactChange, 10))
    if elapsed2 < 200 or elapsedNew2 < 200:
        pygame.draw.rect(screen, RED_BLOOD, (healthBarX2 + p2Health, p2Y - 15, healthChange2, 10))
        pygame.draw.rect(screen, RED_BLOOD, (healthBarX2 + p2Health, p2Y - 15, healthCactChange2, 10))
    
    #health regeneration player 1
    if distance(halfWIDTH, p1X, wellCenterY, p1Y) < 80:
        healing = True
        if helpHealth == 0 and cactCount == 0:
            healthCount = timeNow / 1000
        if timeNow / 1000 == healthCount and p1Health <= 47:
            helpHealth += 1
            healthCount += 1
            p1Health += 2
    else:
        helpHealth = 0
        healing = False
    if healthChange != 0:
        helpHealth = 0
        healthChange = 0

    #health regeneration player 2
    if distance(halfWIDTH, p2X, wellCenterY, p2Y) < 80:
        healing2 = True
        if helpHealth2 == 0 and cactCount2 == 0:
            healthCount2 = timeNow / 1000
        if timeNow / 1000 == healthCount2 and p2Health <= 47:
            helpHealth2 += 1
            healthCount2 += 1
            p2Health += 2
    else:
        helpHealth2 = 0
        healing2 = False
    if healthChange2 != 0:
        helpHealth2 = 0
        healthChange2 = 0

    
    #draw health bars
    pygame.draw.line(screen, BLACK_SECOND, (healthBarX, p1Y - 5),(healthBarX + 50, p1Y - 5),2)
    pygame.draw.line(screen, BLACK_SECOND, (healthBarX2, p2Y - 5),(healthBarX2 + 50, p2Y - 5),2)
    pygame.draw.rect(screen, BLACK, (healthBarX - 1, p1Y - 16, 52, 12),1)
    pygame.draw.rect(screen, BLACK, (healthBarX2 - 1, p2Y - 16, 52, 12),1)
    pygame.draw.rect(screen, GREEN, (healthBarX, p1Y - 15, p1Health, 10))
    pygame.draw.rect(screen, GREEN, (healthBarX2, p2Y - 15, p2Health, 10))

    #in-game information
    textLives1 = font4.render("Lives: ",1,BLACK)
    textWepHeader1 = font4.render("Weapon: ",1,BLACK)
    textWep1 = font3.render(weapon, 1, RED_COPPER)
    
    screen.blit(textLives1,(62,5))
    screen.blit(textWepHeader1,(62,30))
    screen.blit(textWep1, (130, 38))

    textLives2 = font4.render("Lives: ",1,BLACK)
    textWepHeader2 = font4.render("Weapon: ",1,BLACK)
    textWep2 = font3.render(weapon2, 1, BLUE_DARK)
    screen.blit(textLives2,(1007,5))
    screen.blit(textWepHeader2,(1007,30))
    screen.blit(textWep2, (1085, 38))
    for x in range(lives,0,-1):
        screen.blit(badge,(100 + x * (badgeW + 5),5))
    for x in range(lives2):
        screen.blit(badge2,(1085 + x * (badgeW + 5),5))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False
        inPlayMain = False
    play = False
    instruct = False
    back = False
    
    pygame.display.flip() #update entire screen
    
#--------------------------#
#main program begins here
#--------------------------#
while inPlayMain:
    screen.fill(RED)
    pygame.draw.rect(screen, BLACK, (200, 500, 200, 100))
    pygame.draw.rect(screen, BLACK, (900, 500, 200, 100))
    text = font.render("Wild n' Wacky Gunners",1,WHITE)
    text2 = font2.render("Play",1,WHITE)
    text3 = font2.render("Instructions",1,WHITE)
    screen.blit(text, (200, 100))
    screen.blit(text2, (250, 530))
    screen.blit(text3, (920, 530))
    screen.blit(gunsMain,((WIDTH - gunsMainW) / 2, 350))
    screen.blit(coltPortrait,((WIDTH - coltPortraitW) / 2,290))
    pygame.display.update()
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and x <= 400 and x >= 200 and y <= 600 and y >= 500:
            play = True
            break
        if event.type == pygame.MOUSEBUTTONDOWN and x <= 1100 and x >= 900 and y <= 600 and y >= 500:
            instruct = True
            break
    if play:
        break
    if instruct:
        while True:
            screen.fill(GREEN)
            pygame.draw.rect(screen,BLACK,(800, 300, 200, 100))
            text4 = font3.render("This is a 2 player shooter game where you and another player try to kill each other.",1,WHITE)
            text5 = font3.render("You each have 5 lives. You respawn when your health bar goes to 0.",1,WHITE)
            text6 = font3.render("P1: wasd for movement, q for weapon switch, space to shoot.",1,WHITE)
            text7 = font3.render("P2: arrow keys for movement, numpad 4 for weapon switch, 5 to shoot.",1,WHITE)
            text8 = font3.render("Weapon switch only works once all your projectiles are gone and you are not healing.",1,WHITE)
            text9 = font3.render("Cactuses cause damage if you step on them.",1,WHITE)
            text10 = font5.render("P1 is on the left, P2 on the right. May the strongest survive!", 1,WHITE)
            text11 = font2.render("Back",1,WHITE)
            text12 = font4.render("Controls",1,WHITE)
            text13 = font4.render("General",1,WHITE)
            text14 = font4.render("Other",1,WHITE)
            text15 = font6.render("Instructions",1,WHITE)
            screen.blit(text4, (100,180))
            screen.blit(text5, (100,210))
            screen.blit(text6, (100,365))
            screen.blit(text7, (100,395))
            screen.blit(text8, (100,550))
            screen.blit(text9,(100,580))
            screen.blit(text10,(100,650))
            screen.blit(text11, (850, 330))
            screen.blit(text12,(100,315))
            screen.blit(text13,(100,130))
            screen.blit(text14,(100,500))
            screen.blit(text15,(100,50))
            x, y = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and x <= 1000 and x >= 800 and y <= 400 and y >= 300:
                    back = True
                    break
            if back:
                break
            pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False
        inPlayMain = False
    play = False
    instruct = False
    back = False
    
while inPlay:
    #determine if player 1 is touching a cactus and prepare for taking damage
    touchCact = False
    for i in range(20):
        for h in range(cactusXList[i] + 6, cactusXList[i] + 34):
            newCactusY = cactusYList[i] + 4
            newCactusY2 = cactusYList[i] + 30
            if h > p1X and h < p1X + p1W and ((newCactusY > p1Y and newCactusY < p1Y + p1H) or (newCactusY2 > p1Y and newCactusY2 < p1Y + p1H)):
                if dangerCactus == 0:
                    cactCount = 0
                    damageTimeCactus = pygame.time.get_ticks()
                touchCact = True
                dangerCactus = 1                 
    if not(touchCact):
        cactCount = 0
        damageTimeCactus = 0
        dangerCactus = 0

    #same as above for player 2
    touchCact2 = False
    for i in range(20):
        for h in range(cactusXList[i] + 6, cactusXList[i] + 34):
            newCactusY3 = cactusYList[i] + 4
            newCactusY4 = cactusYList[i] + 30
            if h > p2X and h < p2X + p2W and ((newCactusY3 > p2Y and newCactusY3 < p2Y + p2H) or (newCactusY4 > p2Y and newCactusY4 < p2Y + p2H)):
                if dangerCactus2 == 0:
                    cactCount2 = 0
                    damageTimeCactus2 = pygame.time.get_ticks()
                touchCact2 = True
                dangerCactus2 = 1
    if not(touchCact2):
        cactCount2 = 0
        damageTimeCactus2 = 0
        dangerCactus2 = 0
        
    #determine approximate horizontal health bar position based on players' positions
    healthBarX = p1X - (50 - p1W) / 2
    healthBarX2 = p2X - (50 - p2W) / 2
    
    #explosion player 1
    if not(explosion):
        expCount = 0
    if explosion and expCount > 30:
        explosion = False
        expX = -300
        expY = -300
        expDmg = True
        expDmgS = True
    elif explosion:
        expCount = expCount + 1
            
    #explosion player 2
    if not(explosion2):
        expCount2 = 0
    if explosion2 and expCount2 > 30:
        explosion2 = False
        expX2 = -300
        expY2 = -300
        expDmg2 = True
        expDmgS2 = True
    elif explosion2:
        expCount2 = expCount2 + 1

    #determine the healthBarX position in relation to the players' position
    healthBarX = p1X - (50 - p1W) / 2
    healthBarX2 = p2X - (50 - p2W) / 2

    #weapon switch
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and len(bullX) == 0 and len(rocX) == 0:
                if weapon == "Pistol":
                    weapon = "Rocket"
                else:
                    weapon = "Pistol"
            if event.key == pygame.K_KP4 and len(bullX2) == 0 and len(rocX2) == 0:
                if weapon2 == "Pistol":
                    weapon2 = "Rocket"
                else:
                    weapon2 = "Pistol"

    #movement player 1
    collisionXR = p1X + p1W / 2 + p1Speed
    collisionYRL = p1Y + p1H
    collisionXUD = p1X + p1W / 2
    collisionYU = p1Y + p1H - p1Speed
    collisionXL = p1X + p1W / 2 - p1Speed
    collisionYD = p1Y + p1H + p1Speed       
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and p1X < WIDTH - p1W:
        if distance(halfWIDTH, collisionXR, wellCenterY, collisionYRL) > 40 and (distance(tentCenterX,collisionXR,tentCenterY,collisionYRL) > 75) \
         and (distance(tentCenterX2,collisionXR,tentCenterY,collisionYRL) > 75):
            p1X += p1Speed
        coltNum = nextColt[coltNum]
        if direction != "right":
            password = True
            nextColt = [0,1,2,3,4,5,6,7]
            coltNumNew = 0
        direction = "right"
    if keys[pygame.K_w] and p1Y > 0:
        if distance(halfWIDTH, collisionXUD, wellCenterY, collisionYU) > 40 and (distance(tentCenterX,collisionXUD,tentCenterY,collisionYU) > 75) \
            and (distance(tentCenterX2,collisionXUD,tentCenterY,collisionYU) > 75):
            p1Y -= p1Speed
        coltNum = nextColt[coltNum]
        if direction != "up":
            password = True
            nextColt = [0,1,2,3,4,5,6,7]
            coltNumNew = 2
        direction = "up"
    if keys[pygame.K_a] and p1X > 0:
        if distance(halfWIDTH, collisionXL, wellCenterY, collisionYRL) > 40 and (distance(tentCenterX,collisionXL,tentCenterY,collisionYRL) > 75) \
           and (distance(tentCenterX2,collisionXL,tentCenterY,collisionYRL) > 75):
            p1X -= p1Speed
        coltNum = nextColt[coltNum]
        if direction != "left":
            password = True
            nextColt = [0,1,2,3,4,5,6,7]
            coltNumNew = 4
        direction = "left"
    if keys[pygame.K_s] and p1Y < HEIGHT - p1H:
        if distance(halfWIDTH, collisionXUD, wellCenterY, collisionYD) > 40 and (distance(tentCenterX,collisionXUD,tentCenterY,collisionYD) > 75) \
           and (distance(tentCenterX2,collisionXUD,tentCenterY,collisionYD) > 75):
            p1Y += p1Speed
        coltNum = nextColt[coltNum]
        if direction != "down":
            password = True
            nextColt = [0,1,2,3,4,5,6,7]
            coltNumNew = 6
        direction = "down"
    if keys[pygame.K_d] and keys[pygame.K_w]:
        coltNum = nextColt[coltNum]
        if direction != "upright":
            password = True
            nextColt = [0,1,2,3,4,5,6,7]
            coltNumNew = 1
        direction = "upright"
    if keys[pygame.K_a] and keys[pygame.K_w]:
        coltNum = nextColt[coltNum]
        if direction != "upleft":
            password = True
            nextColt = [0,1,2,3,4,5,6,7]
            coltNumNew = 3
        direction = "upleft"
    if keys[pygame.K_a] and keys[pygame.K_s]:
        coltNum = nextColt[coltNum]
        if direction != "downleft":
            password = True
            nextColt = [0,1,2,3,4,5,6,7]
            coltNumNew = 5
        direction = "downleft"
    if keys[pygame.K_d] and keys[pygame.K_s]:
        coltNum = nextColt[coltNum]
        if direction != "downright":
            password = True
            nextColt = [0,1,2,3,4,5,6,7]
            coltNumNew = 7
        direction = "downright"

    #movement player 2
    collisionXR2 = p2X + p2W / 2 + p2Speed
    collisionYRL2 = p2Y + p2H
    collisionXUD2 = p2X + p2W / 2
    collisionYU2 = p2Y + p2H - p2Speed
    collisionXL2 = p2X + p2W / 2 - p2Speed
    collisionYD2 = p2Y + p2H + p2Speed 
    if keys[pygame.K_RIGHT] and p2X < WIDTH - p2W:
        if distance(halfWIDTH, p2X + p2W / 2 + p2Speed, wellCenterY, p2Y + p2H) > 40 and (distance(tentCenterX,collisionXR2,tentCenterY,collisionYRL2) > 75) \
         and (distance(tentCenterX2,collisionXR2,tentCenterY,collisionYRL2) > 75):
            p2X += p2Speed
        coltNum2 = nextColt2[coltNum2]
        if direction2 != "right":
            password2 = True
            nextColt2 = [0,1,2,3,4,5,6,7]
            coltNumNew2 = 0
        direction2 = "right"
    if keys[pygame.K_UP] and p2Y > 0:
        if distance(halfWIDTH, p2X + p2W / 2, wellCenterY, p2Y + p2H - p2Speed) > 40 and (distance(tentCenterX,collisionXUD2,tentCenterY,collisionYU2) > 75) \
            and (distance(tentCenterX2,collisionXUD2,tentCenterY,collisionYU2) > 75):
            p2Y -= p2Speed
        coltNum2 = nextColt2[coltNum2]
        if direction2 != "up":
            password2 = True
            nextColt2 = [0,1,2,3,4,5,6,7]
            coltNumNew2 = 2
        direction2 = "up"
    if keys[pygame.K_LEFT] and p2X > 0:
        if distance(halfWIDTH, p2X + p2W / 2 - p2Speed, wellCenterY, p2Y + p2H) > 40 and (distance(tentCenterX,collisionXL2,tentCenterY,collisionYRL2) > 75) \
           and (distance(tentCenterX2,collisionXL2,tentCenterY,collisionYRL2) > 75):
            p2X -= p2Speed
        coltNum2 = nextColt2[coltNum2]
        if direction2 != "left":
            password2 = True
            nextColt2 = [0,1,2,3,4,5,6,7]
            coltNumNew2 = 4
        direction2 = "left"
    if keys[pygame.K_DOWN] and p2Y < HEIGHT - p2H:
        if distance(halfWIDTH, p2X + p2W / 2, wellCenterY, p2Y + p2H + p2Speed) > 40 and (distance(tentCenterX,collisionXUD2,tentCenterY,collisionYD2) > 75) \
           and (distance(tentCenterX2,collisionXUD2,tentCenterY,collisionYD2) > 75):
            p2Y += p2Speed
        coltNum2 = nextColt2[coltNum2]
        if direction2 != "down":
            password2 = True
            nextColt2 = [0,1,2,3,4,5,6,7]
            coltNumNew2 = 6
        direction2 = "down"
    if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
        if direction2 != "upleft":
            password2 = True
            nextColt2 = [0,1,2,3,4,5,6,7]
            coltNumNew2 = 3     
        direction2 = "upleft"
        coltNum2 = nextColt2[coltNum2]
    if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
        if direction2 != "downleft":
            password2 = True
            nextColt2 = [0,1,2,3,4,5,6,7]
            coltNumNew2 = 5         
        direction2 = "downleft"
        coltNum2 = nextColt2[coltNum2]
    if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
        if direction2 != "upright":
            password2 = True
            nextColt2 = [0,1,2,3,4,5,6,7]
            coltNumNew2 = 1
        direction2 = "upright"
        coltNum2 = nextColt2[coltNum2]
    if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
        if direction2 != "downright":
            password2 = True
            nextColt2 = [0,1,2,3,4,5,6,7]
            coltNumNew2 = 7
        direction2 = "downright"
        coltNum2 = nextColt2[coltNum2]
    
    #add bullet player 1
    if keys[pygame.K_SPACE] and not(healing):
        if status == "ok":
            if direction == "left":
                if weapon == "Pistol":
                    bullX.append(p1X)
                    bullY.append(p1Y+20)
                if weapon == "Rocket":
                    rocX.append(p1X)
                    rocY.append(p1Y+20)
            if direction == "right":
                if weapon == "Pistol":
                    bullX.append(p1X+40)
                    bullY.append(p1Y+20)
                if weapon == "Rocket":
                    rocX.append(p1X+40)
                    rocY.append(p1Y+20)
            if direction == "up":
                if weapon == "Pistol":
                    bullX.append(p1X+20)
                    bullY.append(p1Y)
                if weapon == "Rocket":
                    rocX.append(p1X+20)
                    rocY.append(p1Y)
            if direction == "down":
                if weapon == "Pistol":
                    bullX.append(p1X+20)
                    bullY.append(p1Y+40)
                if weapon == "Rocket":
                    rocX.append(p1X+20)
                    rocY.append(p1Y+40)
            if direction == "upleft":
                if weapon == "Pistol":
                    bullX.append(p1X)
                    bullY.append(p1Y)
                if weapon == "Rocket":
                    rocX.append(p1X)
                    rocY.append(p1Y)
            if direction == "downleft":
                if weapon == "Pistol":
                    bullX.append(p1X)
                    bullY.append(p1Y+40)
                if weapon == "Rocket":
                    rocX.append(p1X)
                    rocY.append(p1Y+40)
            if direction == "upright":
                if weapon == "Pistol":
                    bullX.append(p1X+40)
                    bullY.append(p1Y)
                if weapon == "Rocket":
                    rocX.append(p1X+40)
                    rocY.append(p1Y)
            if direction == "downright":
                if weapon == "Pistol":
                    bullX.append(p1X+40)
                    bullY.append(p1Y+40)
                if weapon == "Rocket":
                    rocX.append(p1X+40)
                    rocY.append(p1Y+40)
            if weapon == "Pistol":
                bullDir.append(direction)
                bullScreen.append(True)
            if weapon == "Rocket":
                rocDir.append(direction)
                rocScreen.append(True)

    #add bullet player 2
    if keys[pygame.K_KP5] and not(healing2):
        if status2 == "ok":
            if direction2 == "left":
                if weapon2 == "Pistol":
                    bullX2.append(p2X)
                    bullY2.append(p2Y+20)
                if weapon2 == "Rocket":
                    rocX2.append(p2X)
                    rocY2.append(p2Y+20)
            if direction2 == "right":
                if weapon2 == "Pistol":
                    bullX2.append(p2X+40)
                    bullY2.append(p2Y+20)
                if weapon2 == "Rocket":
                    rocX2.append(p2X+40)
                    rocY2.append(p2Y+20)
            if direction2 == "up":
                if weapon2 == "Pistol":
                    bullX2.append(p2X+20)
                    bullY2.append(p2Y)
                if weapon2 == "Rocket":
                    rocX2.append(p2X+20)
                    rocY2.append(p2Y)
            if direction2 == "down":
                if weapon2 == "Pistol":
                    bullX2.append(p2X+20)
                    bullY2.append(p2Y+40)
                if weapon2 == "Rocket":
                    rocX2.append(p2X+20)
                    rocY2.append(p2Y+40)
            if direction2 == "upleft":
                if weapon2 == "Pistol":
                    bullX2.append(p2X)
                    bullY2.append(p2Y)
                if weapon2 == "Rocket":
                    rocX2.append(p2X)
                    rocY2.append(p2Y)
            if direction2 == "downleft":
                if weapon2 == "Pistol":
                    bullX2.append(p2X)
                    bullY2.append(p2Y+40)
                if weapon2 == "Rocket":
                    rocX2.append(p2X)
                    rocY2.append(p2Y+40)
            if direction2 == "upright":
                if weapon2 == "Pistol":
                    bullX2.append(p2X+40)
                    bullY2.append(p2Y)
                if weapon2 == "Rocket":
                    rocX2.append(p2X+40)
                    rocY2.append(p2Y)
            if direction2 == "downright":
                if weapon2 == "Pistol":
                    bullX2.append(p2X+40)
                    bullY2.append(p2Y+40)
                if weapon2 == "Rocket":
                    rocX2.append(p2X+40)
                    rocY2.append(p2Y+40)
            if weapon2 == "Pistol":
                bullDir2.append(direction2)
                bullScreen2.append(True)
            if weapon2 == "Rocket":
                rocDir2.append(direction2)
                rocScreen2.append(True)
                

    #pistol player 1
    if weapon == "Pistol":
        for i in reversed(range(len(bullX))):
            if bullDir[i] == "left":
                bullX[i] = bullX[i] - int(1.4*bullSpeed)
            if bullDir[i] == "right":
                bullX[i] = bullX[i] + int(1.4*bullSpeed)
            if bullDir[i] == "up":
                bullY[i] = bullY[i] - int(1.4*bullSpeed)
            if bullDir[i] == "down":
                bullY[i] = bullY[i] + int(1.4*bullSpeed)
            if bullDir[i] == "upleft":
                bullX[i] = bullX[i] - bullSpeed
                bullY[i] = bullY[i] - bullSpeed
            if bullDir[i] == "downleft":
                bullX[i] = bullX[i] - bullSpeed
                bullY[i] = bullY[i] + bullSpeed
            if bullDir[i] == "upright":
                bullX[i] = bullX[i] + bullSpeed
                bullY[i] = bullY[i] - bullSpeed
            if bullDir[i] == "downright":
                bullX[i] = bullX[i] + bullSpeed
                bullY[i] = bullY[i] + bullSpeed

            #pistol damage other player
            for j in range(len(bullX)):
                if bullX[j] >= p2X and bullX[j] <= p2X+p2W and bullY[j] >= p2Y and bullY[j] <= p2Y+p2H:
                    if bullScreen[j]:
                        p2Health -= 2
                        healthChange2 = 2
                        BEGIN2 = pygame.time.get_ticks()
                    bullScreen[j] = False

            #in the case the bullet goes off-screen
            if bullX[i]<0 or bullX[i]>1300 or bullY[i]<0 or bullY[i]>700:
                bullScreen[i] = False

            #collision for player 1 bullet
            if distance(tentCenterX, bullX[i], tentCenterY, bullY[i]) < 75: #first tent 
                bullScreen[i] = False
            if distance(tentCenterX2, bullX[i], tentCenterY, bullY[i]) < 75: #second tent
                bullScreen[i] = False
            if distance(halfWIDTH, bullX[i], wellCenterY, bullY[i]) < 40: #well
                bullScreen[i] = False
            for j in range(20):
                if bullX[i] < cactusXList[j] + 40 and bullX[i] > cactusXList[j] + 6 and bullY[i] > cactusYList[j] + 4 and bullY[i] < cactusYList[j] + 34: #cactus
                    bullScreen[i] = False

            #make necessary changes if necessary to limit pistol's range
            bullDis.append(0)
            bullDis[i] = bullDis[i] + bullSpeed
            bullMax = bullDis[len(bullX)-1]
            if bullDis[i] > 400:
                bullX.pop(i)
                bullY.pop(i)
                bullDis.pop(i)
                bullDir.pop(i)
                bullScreen.pop(i)
            if bullMax < 100:
                status = "fail"
            else:
                status = "ok"

    #rocket player 1
    if weapon == "Rocket":
        for i in reversed(range(len(rocX))):
            if rocDir[i] == "left":
                rocX[i] = rocX[i] - int(1.4*rocSpeed)
            if rocDir[i] == "right":
                rocX[i] = rocX[i] + int(1.4*rocSpeed)
            if rocDir[i] == "up":
                rocY[i] = rocY[i] - int(1.4*rocSpeed)
            if rocDir[i] == "down":
                rocY[i] = rocY[i] + int(1.4*rocSpeed)
            if rocDir[i] == "upleft":
                rocX[i] = rocX[i] - rocSpeed
                rocY[i] = rocY[i] - rocSpeed
            if rocDir[i] == "downleft":
                rocX[i] = rocX[i] - rocSpeed
                rocY[i] = rocY[i] + rocSpeed
            if rocDir[i] == "upright":
                rocX[i] = rocX[i] + rocSpeed
                rocY[i] = rocY[i] - rocSpeed
            if rocDir[i] == "downright":
                rocX[i] = rocX[i] + rocSpeed
                rocY[i] = rocY[i] + rocSpeed
                
            #rocket damage to other player
            for j in range(len(rocX)):
                if rocX[j] >= p2X and rocX[j] <= p2X+p2W and rocY[j] >= p2Y and rocY[j] <= p2Y+p2H:
                    explosion = True
                    if rocScreen[j]:
                        p2Health -= 5
                        healthChange2 = 5
                        BEGIN2 = pygame.time.get_ticks()
                        expX = rocX[j]
                        expY = rocY[j]
                    rocScreen[j] = False

            #in the case the rocket goes off-screen
            if rocX[i]<0 or rocX[i]>1300 or rocY[i]<0 or rocY[i]>700:
                explosion = True
                if rocScreen[i]:
                    expX = rocX[i]
                    expY = rocY[i]
                rocScreen[i] = False

            #collision for player 1 rocket
            if distance(tentCenterX, rocX[i], tentCenterY, rocY[i]) < 75: #first tent
                explosion = True
                if rocScreen[i]:
                    expX = rocX[i]
                    expY = rocY[i]
                rocScreen[i] = False
            if distance(tentCenterX2, rocX[i], tentCenterY, rocY[i]) < 75: #second tent
                explosion = True
                if rocScreen[i]:
                    expX = rocX[i]
                    expY = rocY[i]
                rocScreen[i] = False
            if distance(halfWIDTH, rocX[i], wellCenterY, rocY[i]) < 40: #well
                explosion = True
                if rocScreen[i]:
                    expX = rocX[i]
                    expY = rocY[i]
                rocScreen[i] = False
            for j in range(20):
                if rocX[i] < cactusXList[j] + 40 and rocX[i] > cactusXList[j] + 6 and rocY[i] > cactusYList[j] + 4 and rocY[i] < cactusYList[j] + 34: #cactus
                    explosion = True
                    if rocScreen[i]:
                        expX = rocX[i]
                        expY = rocY[i]
                    rocScreen[i] = False

            #make necessary changes if necessary to limit rocket's range
            rocDis.append(0)
            rocDis[i] = rocDis[i] + rocSpeed
            if rocDis[i] > 400:
                if rocScreen[i]:
                    explosion = True
                    expX = rocX[i]
                    expY = rocY[i]
                rocX.pop(i)
                rocY.pop(i)
                rocDis.pop(i)
                rocDir.pop(i)
                rocScreen.pop(i)
                status = "ok"
            else:
                status = "fail"

            #explosion damage to other player
            for j in range(p2H):
                if distance(expX, p2X, expY, p2Y+j) <= expR:
                    if expDmg:
                        p2Health -= 5
                        healthChange2 = 5
                        BEGIN2 = pygame.time.get_ticks()
                    expDmg = False
            for j in range(p2H):
                if distance(expX, p2X+p2W, expY, p2Y+j) <= expR:
                    if expDmg:
                        p2Health -= 5
                        healthChange2 = 5
                        BEGIN2 = pygame.time.get_ticks()
                    expDmg = False
            for j in range(p2W):
                if distance(expX, p2X+j, expY, p2Y) <= expR:
                    if expDmg:
                        p2Health -= 5
                        healthChange2 = 5
                        BEGIN2 = pygame.time.get_ticks()
                    expDmg = False
            for j in range(p2W):
                if distance(expX, p2X+j, expY, p2Y+p2H) <= expR:
                    if expDmg:
                        p2Health -= 5
                        healthChange2 = 5
                        BEGIN2 = pygame.time.get_ticks()
                    expDmg = False
            
            #self damage
            for j in range(p1H):
                if distance(expX, p1X, expY, p1Y+j) <= expR:
                    if expDmgS:
                        p1Health -= 5
                        healthChange = 5
                        BEGIN = pygame.time.get_ticks()
                    expDmgS = False

            for j in range(p1H):
                if distance(expX, p1X+p1W, expY, p1Y+j) <= expR:
                    if expDmgS:
                        p1Health -= 5
                        healthChange = 5
                        BEGIN = pygame.time.get_ticks()
                    expDmgS = False

            for j in range(p1W):
                if distance(expX, p1X+j, expY, p1Y) <= expR:
                    if expDmgS:
                        p1Health -= 5
                        healthChange = 5
                        BEGIN = pygame.time.get_ticks()
                    expDmgS = False

            for j in range(p1W):
                if distance(expX, p1X+j, expY, p1Y+p1H) <= expR:
                    if expDmgS:
                        p1Health -= 5
                        healthChange = 5
                        BEGIN = pygame.time.get_ticks()
                    expDmgS = False

    #pistol player 2
    if weapon2 == "Pistol":
        for i in reversed(range(len(bullX2))):
            if bullDir2[i] == "left":
                bullX2[i] = bullX2[i] - int(1.4*bullSpeed2)
            if bullDir2[i] == "right":
                bullX2[i] = bullX2[i] + int(1.4*bullSpeed2)
            if bullDir2[i] == "up":
                bullY2[i] = bullY2[i] - int(1.4*bullSpeed2)
            if bullDir2[i] == "down":
                bullY2[i] = bullY2[i] + int(1.4*bullSpeed2)
            if bullDir2[i] == "upleft":
                bullX2[i] = bullX2[i] - bullSpeed2
                bullY2[i] = bullY2[i] - bullSpeed2
            if bullDir2[i] == "downleft":
                bullX2[i] = bullX2[i] - bullSpeed2
                bullY2[i] = bullY2[i] + bullSpeed2
            if bullDir2[i] == "upright":
                bullX2[i] = bullX2[i] + bullSpeed2
                bullY2[i] = bullY2[i] - bullSpeed2
            if bullDir2[i] == "downright":
                bullX2[i] = bullX2[i] + bullSpeed2
                bullY2[i] = bullY2[i] + bullSpeed2

            #damage to player 1 by bullet
            bullDis2.append(0)
            for j in range(len(bullX2)):
                if bullX2[j] >= p1X and bullX2[j] <= p1X+p1W and bullY2[j] >= p1Y and bullY2[j] <= p1Y+p1H:
                    if bullScreen2[j]:
                        p1Health -= 2
                        healthChange = 5
                        damageTime = pygame.time.get_ticks()
                    bullScreen2[j] = False

            #in the case the bullet goes off-screen
            if bullX2[i]<0 or bullX2[i]>1300 or bullY2[i]<0 or bullY2[i]>700:
                bullScreen2[i] = False
                
            #collision for player 2 bullet
            if distance(tentCenterX, bullX2[i], tentCenterY, bullY2[i]) < 75: #first tent
                bullScreen2[i] = False
            if distance(tentCenterX2, bullX2[i], tentCenterY, bullY2[i]) < 75: #second tent
                bullScreen2[i] = False
            if distance(halfWIDTH, bullX2[i], wellCenterY, bullY2[i]) < 40: #well
                bullScreen2[i] = False
            for j in range(20):
                if bullX2[i] < cactusXList[j] + 40 and bullX2[i] > cactusXList[j] + 6 and bullY2[i] > cactusYList[j] + 4 and bullY2[i] < cactusYList[j] + 34: #cactus
                    bullScreen2[i] = False
            
            #make necessary changes if necessary to limit pistol's range
            bullDis2[i] = bullDis2[i] + bullSpeed2
            bullMax2 = bullDis2[len(bullX2)-1]
            if bullDis2[i] > 400:
                bullX2.pop(i)
                bullY2.pop(i)
                bullDis2.pop(i)
                bullDir2.pop(i)
                bullScreen2.pop(i)
            if bullMax2 < 100:
                status2 = "fail"
            else:
                status2 = "ok"

    #rocket player 2
    if weapon2 == "Rocket":
          for i in reversed(range(len(rocX2))):
            if rocDir2[i] == "left":
                rocX2[i] = rocX2[i] - int(1.4 * rocSpeed2)
            if rocDir2[i] == "right":
                rocX2[i] = rocX2[i] + int(1.4 * rocSpeed2)
            if rocDir2[i] == "up":
                rocY2[i] = rocY2[i] - int(1.4 * rocSpeed2)
            if rocDir2[i] == "down":
                rocY2[i] = rocY2[i] + int(1.4 * rocSpeed2)
            if rocDir2[i] == "upleft":
                rocX2[i] = rocX2[i] - rocSpeed2
                rocY2[i] = rocY2[i] - rocSpeed2
            if rocDir2[i] == "downleft":
                rocX2[i] = rocX2[i] - rocSpeed2
                rocY2[i] = rocY2[i] + rocSpeed2
            if rocDir2[i] == "upright":
                rocX2[i] = rocX2[i] + rocSpeed2
                rocY2[i] = rocY2[i] - rocSpeed2
            if rocDir2[i] == "downright":
                rocX2[i] = rocX2[i] + rocSpeed2
                rocY2[i] = rocY2[i] + rocSpeed2
                
            #rocket damage to other player
            for j in range(len(rocX2)):
                if rocX2[j] >= p1X and rocX2[j] <= p1X+p1W and rocY2[j] >= p1Y and rocY2[j] <= p1Y+p1H:
                    explosion2 = True
                    if rocScreen2[j]:
                        p1Health -= 5
                        healthChange = 5
                        BEGIN = pygame.time.get_ticks()
                        expX2 = rocX2[j]
                        expY2 = rocY2[j]
                    rocScreen2[j] = False

            #in the case the rocket goes off-screen
            if rocX2[i]<0 or rocX2[i]>1300 or rocY2[i]<0 or rocY2[i]>700:
                explosion2 = True
                if rocScreen2[i]:
                    expX2 = rocX2[i]
                    expY2 = rocY2[i]
                rocScreen2[i] = False

            #collision for player 2 rocket
            if distance(tentCenterX, rocX2[i], tentCenterY, rocY2[i]) < 75: #first tent
                explosion2 = True
                if rocScreen2[i]:
                    expX2 = rocX2[i]
                    expY2 = rocY2[i]
                rocScreen2[i] = False
            if distance(tentCenterX2, rocX2[i], tentCenterY, rocY2[i]) < 75: #second tent
                explosion2 = True
                if rocScreen2[i]:
                    expX2 = rocX2[i]
                    expY2 = rocY2[i]
                rocScreen2[i] = False
            if distance(halfWIDTH, rocX2[i], wellCenterY, rocY2[i]) < 40: #well
                explosion2 = True
                if rocScreen2[i]:
                    expX2 = rocX2[i]
                    expY2 = rocY2[i]
                rocScreen2[i] = False
            for j in range(20):
                if rocX2[i] < cactusXList[j] + 40 and rocX2[i] > cactusXList[j] + 6 and rocY2[i] > cactusYList[j] + 4 and rocY2[i] < cactusYList[j] + 34: #cactus
                    explosion2 = True
                    if rocScreen2[i]:
                        expX2 = rocX2[i]
                        expY2 = rocY2[i]
                    rocScreen2[i] = False

            #make necessary changes if necessary to limit pistol's range
            rocDis2.append(0)
            rocDis2[i] = rocDis2[i] + rocSpeed2
            if rocDis2[i] > 400:
                if rocScreen2[i]:
                    explosion2 = True
                    expX2 = rocX2[i]
                    expY2 = rocY2[i]
                rocX2.pop(i)
                rocY2.pop(i)
                rocDis2.pop(i)
                rocDir2.pop(i)
                rocScreen2.pop(i)
                status2 = "ok"
            else:
                status2 = "fail"

            #explosion damage to other player
            for j in range(p1H):
                if distance(expX2, p1X, expY2, p1Y+j) <= expR2:
                    if expDmg2:
                        p1Health -= 5
                        healthChange = 5
                        BEGIN = pygame.time.get_ticks()
                    expDmg2 = False

            for j in range(p1H):
                if distance(expX2, p1X+p1W, expY2, p1Y+j) <= expR2:
                    if expDmg2:
                        p1Health -= 5
                        healthChange = 5
                        BEGIN = pygame.time.get_ticks()
                    expDmg2 = False

            for j in range(p1W):
                if distance(expX2, p1X+j, expY2, p1Y) <= expR2:
                    if expDmg2:
                        p1Health -= 5
                        healthChange = 5
                        BEGIN = pygame.time.get_ticks()
                    expDmg2 = False

            for j in range(p1W):
                if distance(expX2, p1X+j, expY2, p1Y+p1H) <= expR2:
                    if expDmg2:
                        p1Health -= 5
                        healthChange = 5
                        BEGIN = pygame.time.get_ticks()
                    expDmg2 = False

            #self damage
            for j in range(p2H):
                if distance(expX2, p2X, expY2, p2Y+j) <= expR2:
                    if expDmgS2:
                        p2Health -= 5
                        healthChange2 = 5
                        BEGIN2 = pygame.time.get_ticks()
                    expDmgS2 = False

            for j in range(p2H):
                if distance(expX2, p2X+p2W, expY2, p2Y+j) <= expR2:
                    if expDmgS2:
                        p2Health -= 5
                        healthChange2 = 5
                        BEGIN2 = pygame.time.get_ticks()
                    expDmgS2 = False

            for j in range(p2W):
                if distance(expX2, p2X+j, expY2, p2Y) <= expR2:
                    if expDmgS2:
                        p2Health -= 5
                        healthChange2 = 5
                        BEGIN2 = pygame.time.get_ticks()
                    expDmgS2 = False

            for j in range(p2W):
                if distance(expX2, p2X+j, expY2, p2Y+p2H) <= expR2:
                    if expDmgS2:
                        p2Health -= 5
                        healthChange2 = 5
                        BEGIN2 = pygame.time.get_ticks()
                    expDmgS2 = False
                    
    #exit program if escape is pressed
    if keys[pygame.K_ESCAPE]:
        inPlay = False

    #preparations for end screen
    if lives == 0:
        inPlay = False
        p2Win = True
        gameOver = True
    if lives2 == 0:
        inPlay = False
        p1Win = True
        gameOver = True
    redrawScreen()

    #slight delay
    wait = 12
    pygame.time.delay(wait)

#game over screen
while gameOver:
    screen.fill(RED)
    pygame.draw.rect(screen, BLACK, (550, 500, 200, 100))
    pygame.draw.rect(screen, BROWN, (420, 30, 400, 180))
    text100 = font.render("GAME OVER!", 1, WHITE)
    if p1Win:
        text101 = font2.render("P1 wins! P2, YOU LOSE!!!", 1, WHITE)
        screen.blit(coltPic[6], (200, 400))
        if loserBlit:
            screen.blit(coltPic[6], (900, 400))
        pygame.draw.circle(screen, BLACK, (950, boulderY), 100)
        boulderY += 1
        if boulderY >= 400:
            loserBlit = False
    elif p2Win:
        text101 = font2.render("P2 wins! P1, YOU LOSE!!!", 1, WHITE)
        screen.blit(coltPic2[6], (200, 400))
        if loserBlit:
            screen.blit(coltPic2[6], (900, 400))
        pygame.draw.circle(screen, BLACK, (950, boulderY), 100)
        boulderY += 1
        if boulderY >= 400:
            loserBlit = False
    text102 = font2.render("Exit Game", 1, WHITE)
    text103 = font3.render("Created by Matthew Sekirin and Andy Li", 1, WHITE)
    text104 = font3.render("If you use our game name you will be sued for copyright", 1, WHITE)
    screen.blit(text100, (430, 50))
    screen.blit(text101, (450, 150))
    screen.blit(text102, (570, 520))
    screen.blit(text103, (440, 300))
    screen.blit(text104, (420, 400))
    
    pygame.display.update()
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and x <= 750 and x >= 550 and y <= 600 and y >= 500:
            gameOver = False

pygame.quit()

