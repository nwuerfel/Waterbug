import getopt, sys, datetime
import random as rand
import math

helpMessage = 'usage: <cmdline> python waterBug.py -b <number of bugs> -l <number of turns in sim> -h for help'

# waterBug class barebones atm
class waterBug:
    def __init__(self, vel=0, theta=0, xPos=0, yPos=0, radius=.1, num=0):
        self.vel = vel
        self.theta = theta
        self.xPos = xPos
        self.yPos = yPos
        self.radius = radius
        self.num = num

# river class, can inculde a current but presently only defines width and height
class riverObj:
    def __init__(self, width=2, height=2, current=0):
        self.width = width
        self.height = height

# randSpawn() returns the initial conditions suitable for generation of a new
# bug, later should match up to expected vals or seeds or something
def randSpawn(maxWidth, maxHeight):
    vel = 0
    theta = 2*math.pi*round(rand.random(),6)
    xPos = maxWidth*round(rand.random(),6)
    yPos = maxHeight*round(rand.random(),6)
    radius = .01
    return [vel, theta, xPos, yPos, radius]

# fundamental loop that handles turns and prints sim values to the outfile
def loop(river, bugList, outFile, turnCount):

    # write turn header
    outFile.write('Turn %i\n' % turnCount)

    # write moves for the turn
    for bug in bugList:

        # first, move the bug
        
        # make bug jump randomly
        if rand.random() < 0.5:
            bug.vel = bug.vel+.10

        bug.xPos = bug.xPos + 
           
        # check for, and resolve collisions
        #TODO
        # record results for the bug's round
        outFile.write('%4f %4f %4f %4f %i\n' % (bug.vel, bug.theta, bug.xPos, bug.yPos, bug.num))
    return

# main
def main(argv):
    now = datetime.datetime.now()
    numBugs = 0
    bugList = []
    simLen = 100
    outFileName = '../simFiles/defaultOut.wb'

    # UI bullshit
    try:
        opts, args = getopt.getopt(argv, "hb:l:o:")    
    except getopt.GetoptError:
        print helpMessage
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print helpMessage
            sys.exit()
        elif opt == '-b':
            numBugs = int(arg)
        elif opt == '-l':
            simLen = int(arg)
        elif opt == '-o':
            outFileName = '../simFiles/' + arg
            
    # generate the data header
    # data header currently just gives time of the simulation and numbugs
    header = now.strftime("%Y-%m-%d %H:%M") + ' %d\n' % numBugs 

    # open file to store values for later playback
    with open(outFileName,'w') as outFile:
    
        # write file header with info about the simulation
        outFile.write(header) 

        # construct river
        river = riverObj()

        # construct bugs
        for i in range(numBugs):
            [vel, theta, xPos, yPos, radius] = randSpawn(river.width, river.height)
            newBug = waterBug(vel, theta, xPos, yPos, radius, i) 
            bugList.append(newBug)
        
        # run the main loop as many times as specified
        for i in range(simLen):
            loop(river, bugList, outFile, i)

    print 'Thanks for playing... see you next time.'

if __name__ == "__main__":
    main(sys.argv[1:])
