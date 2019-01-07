import random
import time

# check if target in muyList
def inList(myList, target): 
    for i in myList: 
        if (i == target): 
            return True
    return False

# print a multiplication between i and j 
def printQuestion(i, j):
    print("What is", i, " x ", j, " ?") 


# print possible answers 
def printOptions(myList): 
    for i in range(len(myList)): 
        print(chr((ord('a') + i)), myList[i])


def answerList(number, myList): 
    result = []
    for i in myList: 
        result.append(number * i)
    return result

# return a list of possible answer 
def createOption(i, j): 
    result = []
    result.append(i*j)
    for duration in range(3):
        temp = random.randint(1,9)

        while(True):
            temp = random.randint(1,9)
            if inList(result, temp):
                continue
            break
        result.append(i * temp) 
    return result 

def checkAnswer(myAnswerIndex, myList, number, target):
    if myList[myAnswerIndex] == number * target:
        return True
    return False




print("Welcome to Multiplication Game")
progress = [ [0 for i in range(9)] for j in range(9)] 
while(True):
    number = input("Which number do you want to learn? ")
    number = int(number)
    if number <0 or number > 9: 
        print("Please input number from 1 to 9")
        continue
    break 
time.sleep(1)

print("Are you ready?")
fromZeroToNine = list(range(0,9))
random.shuffle(fromZeroToNine)
for i in fromZeroToNine:
    options = createOption(number, i)
    random.shuffle(options)
    printQuestion(number, i)
    printOptions(options)
    your_answer= input("What is the correct answer? a, b, c ,d")
    your_answer_index = ord(your_answer) - ord('a')
    #print ("*****",your_answer_index)
    if (checkAnswer(your_answer_index, options, number, i)):
        print(your_answer ,"That's the correct answer ")
    else:
        print(your_answer, "Sorry, This is not correct")
    print("***************************")
    print()








