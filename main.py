#-----------------------------------------------------------------------------
# Name:        Kangaroo Long Jump Simulator
# Purpose:     My program for the Project: Putting It All Together assignemnt.
#              This program simulates the growth of a kangaroo. The goal is to
#              Successfuly jump to grab food and avoid obstaclesto grow.
#
# Author:      Danny Kenneth
# Created:     14-Apr-2025
# Updated:     23-May-2025
#-----------------------------------------------------------------------------
# #importing the random library to create a probability system for different obstacles
import random
#importing the math library for physics calculations
import math

# delcaring primary dictionary
kangaroo = {
    "name": "",
    "species": "Western Grey Kangaroo",
    "height": 1.0,
    "power": 30.0,
    "level": 1,
    "levelPercent": 0,
    "health": 4,
    "maxHealth": 4,
    "hunger": 3,
    "maxHunger": 3,
    "highest": 0
}

#declaring the dictionary containing information for multiple kangaroo species
# height, power, health, hunger 
kangaroos_info = {
    'Red Kangaroo': (1.0, (50.0, 70.0, 85.0), (7, 10, 12), (5, 7, 8)),
    'Eastern Grey Kangaroo': (1.0, (42.0, 58.0, 70.0), (6, 8, 10), (4, 6, 7)),
    'Western Grey Kangaroo': (1.0, (30.0, 40.0, 50.0), (4, 6, 7), (3, 5, 6)),
    'Antilopine Kangaroo': (1.0, (36.0, 50.0, 60.0), (5, 7, 8), (4, 5, 6)),
}

# declaring a list with the number of successful scenarios to reach next level
levelUp = [1, 2, 3, 5, 5, 5, 5, 6, 7, 10]

#declaring other important variables for the program
userInput = ''
kangarooTypeInput = ''
angleInput = ''
successfulScenarios = 0
startGame = False
gameType = ''
exitLoop = False


#2D Kinematic variables needed for calculations
gravity_constant = 9.8
angle =  -1
distance = 0
maxDistanceCm = 0
gapDistance = 0
score = 0

#Declaring variables for angle choices
optionsList = []

#defining functions
def readData(file):
    '''
    Reads the data in a agiven text file and returns a list of all values or 

    Parameters
    -------
    file: string

    Returns
    newData: list[str]
        All the data from a text file consolidated into a list
    '''
    newData = []
    try:
        with open(file, 'r') as dataFile:
            data = dataFile.readlines()
            for item in data:
                newData.append(item.strip())
        return newData
    except FileNotFoundError as error:
        print(f"An error has occurred: {error}")
        return []
    finally:
        dataFile.close()


def readStory(start, end, type, addInput = True, formatVar = ''):
    '''
    Prints out certain statements from the story text file

    Parameters
    -------
    start: int
    end: int
    type: str
    addInput: bool, optional
    formatVar: variable name, optional

    Returns
    -------
    None
        This function automatically prints statements or inputs instead of returning a value

    Raises
    -------
    ValueError
        If type does not equal "print" or "input"
    '''
    storyData = readData('story.txt')
    if type == 'print':
        print("--------------------------------------------------------------------------------------------------------------")
        print(f"| ✨ {kangaroo['level']} {kangaroo['levelPercent']}% | {kangaroo['hunger'] * '🍗'} | {kangaroo['health'] * '❤️ '}  | ↕ {kangaroo['height']}m | 💥 {kangaroo['power']} |")
        for i in range(start - 1, end):
            if formatVar == '':
                print(storyData[i])
            else:
                print(storyData[i].format(formatVar))
            if addInput:
                input("Continue > ")
    elif type == 'input':
        for x in range(start - 1, end):
            if formatVar == '':
                input(storyData[x])
            else:
                input(storyData[x].format(formatVar))
    else:
        raise ValueError('The given value for "type" does not match the accepted vales "print" or "input".')

    
    print("--------------------------------------------------------------------------------------------------------------")

def convert(value):
    '''
    Converts a value from a string to an int, float, bool, None, or str based on its value

    Parameters
    -------
    value: str

    Returns
    -------
    True
        If 'value' is the bool value of True

    False
        If 'value' is the bool valye of False

    None
        If 'value' is None 
    
    int
        If 'value' is supposed to be an int
    
    float
        If 'value' is supposed to be a float

    str:
        If the value cannot be converted to any of the other types mentioned above
    '''
    if value == "True":
        return True
    elif value == "False":
        return False
    elif value == "None":
        return None
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value


def save():
    '''
    Saves current data into a seperate text file

    Parameters
    -------
    None

    Returns
    -------
    None
    '''
    with open("save.txt", "w") as saveFile:
        for key, value in kangaroo.items():
            saveFile.write(f"{key}|{value}\n")
    print("Your progress has been saved")


def continueGame():
    '''
    Recieves data from the save text file and imports it into the main dictionary

    Parameters
    -----
    None

    Returns
    -------
    startGame: bool
        Returns true when ready to begin the game
    '''
    
    saveDataFile = readData('save.txt')
    for line in saveDataFile:
        key, value = line.strip().split("|", 1)
        kangaroo[key] = convert(value)
    print("Data successfully loaded.")
    input("Continue > ")



# The main program begins here
print("--------------------------------------------------------------------------------------------------------------")
print("| KANGAROO LONG JUMP SIMULATOR                                                                               |")
print("|                                                                                                            |")
print("| Press Enter to Comtinue                                                                                    |")
userInput = input("| > ")
print("--------------------------------------------------------------------------------------------------------------")
print("| Please choose one of the two options below.                                                                |")
print("|                                                                                                            |")
print("|                                                                                                            |")
print("|                                                                                                            |")
print("|                              NEW GAME: N                            CONTINUE GAME: C                       |")
print("|                                                                                                            |")
print("|                                                                                                            |")
print("|                                                                                                            |")
print("--------------------------------------------------------------------------------------------------------------")
gameType = input("Choose one (N, C) > ")

if gameType == 'C':
    try:
        continueGame()
    except (FileNotFoundError, AttributeError):
        print("You do not have any existing accounts, a new game will be made instead.")
        gameType = 'N'

if gameType == 'N':
    # for any readStory() functions, check the story.txt file to see the story. Number listed coresponds to line number in the file.
    readStory(1, 4, 'print')

    while userInput != "Y":
        readStory(5, 5, 'print', False)
        kangaroo["name"] = input("| Name: ")
        readStory(6, 6, 'print', False, kangaroo['name'])
        print(f"| Y|N")
        userInput = input("| > ")

    #writing info and determining the kangaroo that will be used for the game. Each kangaroo has differetn stats and abilities based on their real life characteristics

    readStory(7, 11, 'print', False)
    readStory(12, 12, 'input')
    readStory(13, 16, 'print', False)
    readStory(17, 17, 'input')
    readStory(18, 21, 'print', False)
    readStory(22, 22, 'input')
    readStory(23, 26, 'print', False)
    readStory(27, 27, 'input')
    readStory(28, 31, 'print')
    kangarooTypeInput = input('Type the kangaroo type here: ')  

    #changing kangaroo stats based on the kangaroo chosen
    try:
        height, power, health, hunger = kangaroos_info[kangarooTypeInput]
    except KeyError:
        print("Since an input wasn't given for the kangaroo species, the Western Grey Kangaroo was chosen.")
        kangarooTypeInput = 'Western Grey Kangaroo'
        height, power, health, hunger = kangaroos_info[kangarooTypeInput]
    kangaroo['height'] = height
    stageOnePower, stageTwoPower, stageThreePower = power
    stageOneHealth, stageTwoHealth, stageThreeHealth = health
    stageOneHunger, stageTwoHunger, stageThreeHunger = hunger
    kangaroo['power'] = stageOnePower
    kangaroo['health'] = stageOneHealth
    kangaroo['maxHealth'] = stageOneHealth
    kangaroo['hunger'] = stageOneHunger
    kangaroo['maxHunger'] = stageOneHunger

#starting the main game loop. This loop runs when health is greater than 0.
while kangaroo["health"] > 0:
    # determining the scenario that will run
    scenario = random.randint(0, 2)
    # determining the difference based on kangaroo level
    if scenario <= 1:
        maxDistanceCm = math.floor((kangaroo['power'] / gravity_constant) * 100)
        distance = random.randint(0, maxDistanceCm)
    
    # changing the messahe given to the user based on teh scenario
    if scenario == 0:
        readStory(32, 32, 'print', True, distance / 100)
        readStory(33, 34, 'print')

    if scenario == 2:
        readStory(43, 43, 'print')

    #determining angle of projection to safely hit obstacle/food
    value = ((distance / 100) * gravity_constant) / kangaroo["power"]
    if -1 <= value <= 1:
        angle_radians = 0.5 * math.asin(value)
        angle = math.floor(math.degrees(angle_radians))
    else:
        readStory(44, 44, 'print')

    # creating game mechanics based on scenario
    # scenario 1 will give you a choice between 3 angles to jump from. You win by guessing the right ang;e
    if scenario == 0:
        optionOne = angle
        optionTwo = angle
        correctAnglePosition = random.randint(0, 2)
        while angle - 2 < optionOne < angle + 2:
            optionOne = random.randint(0, 45)
        while angle - 2 < optionTwo < angle + 2:
            optionTwo = random.randint(0,45)
        #creating a randomized list for the 3 options
        if correctAnglePosition == 0:
            optionsList.append(angle)
            optionsList.append(optionOne)
            optionsList.append(optionTwo)
        elif correctAnglePosition == 1:
            optionsList.append(optionOne)
            optionsList.append(angle)
            optionsList.append(optionTwo)
        else:
            optionsList.append(optionOne)
            optionsList.append(optionTwo)
            optionsList.append(angle)
    
        readStory(45, 45, 'print', False)
        print(f"{optionsList[0]}, {optionsList[1]}, {optionsList[2]}.")

        # make this message loop when the player does not give an integer value
        angleInput = None
        hintsUsed = 0
        while not isinstance(angleInput, int):
            loopedInput = input("Hint or angle> ")
            if loopedInput == 'hint':
                if hintsUsed == 0:
                    readStory(35, 35, 'print')
                elif hintsUsed == 1:
                    readStory(36, 36, 'print')
                else:
                    readStory(37, 37, 'print')
                hintsUsed += 1
            else:
                try:
                    angleInput = int(loopedInput)
                except ValueError:
                    print("Please enter a valid number or 'hint'.")
        if angleInput == angle:
            if kangaroo["health"] < 5:
                kangaroo["health"] += 1
            successfulScenarios += 1
            optionsList.clear()
            readStory(46, 46, 'print')
        else:
            kangaroo['hunger'] -= 1
            optionsList.clear()
            readStory(47, 47, 'print')

    if scenario == 1:
        hintsUsed = 0

        while True:
            readStory(38, 38, 'print', True, distance / 100)
            readStory(48, 48, 'print', False)
            readStory(39, 39, 'print')
            angleInput = input("Hint or angle> ")
            
            if angleInput == 'hint':
                if hintsUsed == 0:
                    readStory(40, 40, 'print')
                elif hintsUsed == 1:
                    readStory(41, 41, 'print')
                else:
                    readStory(42, 42, 'print')  
                hintsUsed += 1
            else:
                try:
                    newAngleInput = int(angleInput)
                    break
                except ValueError:
                    print("Please enter a valid number or type 'hint'.")
        if newAngleInput > angle:
            radians = math.radians(angle)
            gapDistance = math.floor(((kangaroo['power'] * math.sin(2 * radians)) / gravity_constant) * 100)
            score = 867 - gapDistance
            if score > kangaroo['highest']:
                kangaroo['highest'] = score
            successfulScenarios += 1
            readStory(49, 49, 'print', False)
            readStory(50, 50, 'print', False, gapDistance / 100)
            readStory(51, 51, 'print', True, kangaroo['highest'])
        else:
            kangaroo['health'] -= 1
            readStory(52, 53, 'print', False)

    #Changing the levelPercent based on the ratio between completed scemarios and number of completed scenarios required to level up
    kangaroo['levelPercent']  = math.floor(100 * (successfulScenarios / levelUp[kangaroo['level'] - 1]))

    #Decreasing health every time the player contumues failing when they have 0 hunger
    if kangaroo['hunger'] <= 0:
        kangaroo['health'] -= 1

    #Increasing the level if the player successfully beats x scenatrios
    if successfulScenarios >= levelUp[kangaroo['level'] - 1]:
        kangaroo['level'] += 1
        successfulScenarios = 0
        kangaroo['health'] = kangaroo['maxHealth']
        kangaroo['hunger'] = kangaroo['maxHunger']
        kangaroo['levelPercent'] = 0
        if kangaroo['level'] == 6:
            kangaroo['power'] = stageTwoPower
            kangaroo['health'] = stageTwoHealth
            kangaroo['maxHealth'] = stageTwoHealth
            kangaroo['hunger'] = stageTwoHunger
            kangaroo['maxHunger'] = stageTwoHunger
            readStory(54, 54, 'print', False)
            readStory(55, 55, 'print', False, kangaroo['power'])
            readStory(56, 56, 'print', False, kangaroo['health'])
            readStory(57, 57, 'print', True, kangaroo['hunger'])
        elif kangaroo['level'] == 9:
            kangaroo['power'] = stageThreePower
            kangaroo['health'] = stageThreeHealth
            kangaroo['maxHealth'] = stageThreeHealth
            kangaroo['hunger'] = stageThreeHunger
            kangaroo['maxHunger'] = stageThreeHunger
            readStory(58, 58, 'print', False)
            readStory(55, 55, 'print', False, kangaroo['power'])
            readStory(56, 56, 'print', False, kangaroo['health'])
            readStory(57, 57, 'print', True, kangaroo['hunger'])
        else:
            readStory(59, 59, 'print', True, kangaroo['level'])

    #This is the extra action section. This is where asving and exiting can happen
    actionInput = None
    readStory(61, 62, 'print', False)
    while actionInput != '': 
        actionInput = input("Type something or press enter > ")
        if actionInput == 'save':
            save()
        elif actionInput == 'exit':
            readStory(63, 64, 'print', False)
            userInput = input("> ")
            if userInput == 'Y':
                readStory(67, 67, 'print', False, kangaroo['highest'])
                exit()
        elif actionInput == 'delete':
            readStory(65, 66, 'print', False)
            userInput = input("> ")
            if userInput == 'Y':
                open('save.txt', 'w').close()
                print("| Your data has been successfully erased.")
        elif actionInput != '':
            print("| That is an invalid function. Please try again.")
                

# creating the game over screen when health is at or below 0
if kangaroo['health'] <= 0:
    readStory(60, 60, 'print', False, kangaroo['highest'])
