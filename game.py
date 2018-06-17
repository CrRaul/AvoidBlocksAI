import pygame
import random

from NeuralNetwork import NeuralNetwork
pygame.init()
win = pygame.display.set_mode((450, 510))
pygame.display.set_caption("Craioveanu Raul - ")
pygame.display.update()

lovit = False
WINWIDTH = 450
WINHEIGHT = 500
WINMIDDLE = 200
DIMENSION = 10
TIME = 0
MOVE = 0 
SPEED = 3
xAI = 200
yAI = 450



# Desc:     change position of ai
# In:       direction of AI: 0 -up; 1-right; 2-down; 3-left; 4-stay
# Out:      --
def move(direction):
    global WINWIDTH, WINHEIGHT, WINMIDDLE ,NUMOPPONENTS, TIME, MOVE, SPEED, xAI, yAI

    if direction == 0:
        if yAI - SPEED >= WINMIDDLE:
            yAI -= SPEED
            MOVE += 1
    if direction == 1:
        if xAI + SPEED <= WINWIDTH:
            xAI += SPEED
            MOVE += 1
    if direction == 2:
        if yAI + SPEED <= WINHEIGHT:
            yAI += SPEED
            MOVE += 1
    if direction == 3:
        if xAI - SPEED >= 0:
            xAI -= SPEED
            MOVE += 1
    if direction == 4:
        pass


#   draw all elem in windows
def drawWin(opponents):
    global WINWIDTH, WINHEIGHT, WINMIDDLE ,NUMOPPONENTS, TIME, MOVE, SPEED, xAI, yAI,  lovit

    win.fill((0,0,0))
    
    app = pygame.Rect(xAI, yAI, DIMENSION,DIMENSION)
    if lovit == False:
        win.fill((255,0,0), app)
    else:
        win.fill((0,0,255), app)
        pygame.time.wait(500)
        lovit = False

    for i in range(0, 3):
        app = pygame.Rect(opponents[i][0], opponents[i][1],DIMENSION, DIMENSION)
        win.fill((124,252,0), app)

    pygame.display.update()


def run():
    global WINWIDTH, WINHEIGHT, WINMIDDLE ,NUMOPPONENTS, TIME, MOVE, SPEED, xAI, yAI, DIMENSION, lovit
    

    # SET WEIGHTS......
    weightsIH = [[0.028505802192455132,0.17376547912101015,1.1762732006432781,0.5537700706276238,1.1309212918997276,-0.5897716231089585,-0.9798426449379163,-0.4310409052609101,0.5220862186907342,-0.31830235360927417,-1.2027454390416432,0.9283816469271171],
                [1.8630660096883327,0.48229758464004235,0.36772957159338393,0.07218502250689207,-0.23833135080110246,-0.551792253981102,1.1184752390699075,-0.8193570142225324,-0.023295367115428123,-0.07258239128831301,-0.4942117579536853,0.6420393880641213],
                [1.5428670088327134,-0.6317210779870761,-0.9336535627061826,0.4759930903102312,0.6183721303740874,-0.3280254885432339,0.5965015448583542,-0.7287912839146611,0.4788919650232686,-0.8059363598892333,0.3062401327440669,-0.4206000997197281],
                [0.5730983145485484,-0.5473658146807339,-0.7672327279241176,-1.22139607065318,0.9272386607546126,-0.8506212662297723,0.41883394167024224,0.18166008524078348,-0.821572578380749,1.2866980395274654,-1.3287976629390508,0.5110311515681312],
                [-0.16674897768417463,1.5297755235767023,-0.0012851731357645946,1.2645829915473,-0.2030217570053996,-0.07725951437233158,-0.6482536857102132,0.6166555316408859,-0.03958807746395654,-1.16787126165831,1.089929993223436,-0.9868981380318833],
                [-0.5308101120587301,-0.9913698224057068,-1.769744643996798,0.6790783741475341,0.7304120098685771,-0.8465925903779083,-0.3252008881363586,-0.3255133903728271,-0.3967388859719596,-1.5852244202504933,0.302548363163192,0.7060787281872862],
                [0.9132254742162327,-0.809010808825142,-0.46088741710088277,-0.5734534041128547,-0.41188999264494064,-0.9439716825398774,-0.5776285171642186,0.8982076565784636,-0.18681583844076122,0.7638117013355645,-0.13792082620498447,-0.13303215689255898],
                [0.3989914118155322,0.5817302620648048,0.2750923504169378,-0.019512897189301492,0.2076310930247931,-0.9346984060397581,-0.6980323185321882,0.1361514369378567,0.6710991716104806,-0.3097432344352602,0.1821771030822381,-0.8299193120320345]]

    weightsHO = [[-0.9325937487934486,-0.5511883654090097,0.8156652663775723,0.41484920310826,0.33986794606362847,0.5425735337723847,-0.946407430489544,0.39198342630848604],
                [0.3553841337910759,-0.0031602569274287173,-0.054926659274732836,-0.7144786569280299,0.5813598189343978,-1.7755869269507967,0.24673829560368565,0.859492294978041],
                [0.04379587800596485,-0.5710458236462923,0.6655983459375385,-0.2289797178421038,-0.3771212573864302,-0.16570273666630375,-0.8351753697515192,0.38425071988166337],
                [-0.9418025925604014,0.9926500020003344,2.080229478189919,0.7381403512265421,0.30528405213417464,0.19448136157025964,0.6361367370910134,0.25096166156153643],
                [-1.042356013099464,0.8940944694802848,-1.5083425840382472,-0.3671607063668503,-1.8912932386685948,-0.3404474281166765,-0.7860565698725799,-0.2147729095746167]]

    nn = NeuralNetwork(12,8,5)

    for i in range(0, nn.getDimensionWeightsIH()[0]):
        for j in range(0, nn.getDimensionWeightsIH()[1]):
            nn.setWeightIHPos(i,j,weightsIH[i][j])
    for i in range(0, nn.getDimensionWeightsHO()[0]):
        for j in range(0, nn.getDimensionWeightsHO()[1]):
            nn.setWeightHOPos(i,j,weightsHO[i][j])
    #=====================================================================================


    gameExit = False
    


    # opponents[i][0] is x coord of i opponent
    # opponents[i][1] is y coord of i opponent
    opponents = []
    opponents.append([random.randint(1, WINWIDTH), random.randint(1, WINMIDDLE)])
    opponents.append([random.randint(1, WINWIDTH), random.randint(1, WINMIDDLE)])
    opponents.append([random.randint(1, WINWIDTH), random.randint(1, WINMIDDLE)])

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
        
        pygame.time.wait(4)

        drawWin(opponents)

        # create the inputs for neuralNetwork
        inputs = []
        inputs.append(xAI + DIMENSION//2)                    # distance from leftLimit to AI
        inputs.append(yAI + DIMENSION//2 - WINMIDDLE)       # distance from middleLimit to AI
        inputs.append(WINWIDTH - xAI + DIMENSION//2)         # distance from AI to rightLimit
        inputs.append(WINHEIGHT - yAI + DIMENSION//2)        # distance from AI to downLimit

        for i in range(0, len(opponents)):
            inputs.append(xAI - opponents[i][0])     # x - distance from opponent i to AI  
            inputs.append(yAI - opponents[i][1])     # y - distance from opponent i to AI
               
        inputs.append(SPEED)
        inputs.append(DIMENSION)

        # receive the output from NeuralNetwork
        outputs = nn.feedForward(inputs)

        
        # make the best decision( val of output) ( outputs[0] => go up....)
        posMove = 0
        valMove = 0
        for i in range(0,len(outputs)):
            if outputs[i] > valMove:
                valMove = outputs[i]
                posMove = i

        print(posMove)

        # moveAI
        move(posMove)

        # move opponent
        for i in range(0, len(opponents)):
            if opponents[i][0] != 0:
                opponents[i][1] += SPEED
        
        # verify if AI crash
        for i in range(0, len(opponents)):
            oppC = opponents[i]
            if oppC[0] < xAI or oppC[0] > xAI + DIMENSION:
                continue
            if oppC[1] < yAI or oppC[1] > yAI + DIMENSION:
                continue
            lovit = True   
        
        

        # verify if opponent cross the downLine
        for i in range(0, len(opponents)):
            if opponents[i][1] > WINHEIGHT:
                opponents[i][1] = random.randint(1, WINMIDDLE)
                opponents[i][0] = random.randint(1, WINWIDTH) 

         
run()