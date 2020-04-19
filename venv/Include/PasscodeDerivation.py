import os, sys

#open and read file
#in case of manual address imput: filePath = "C:\\Users\\...\\p079_keylog.txt"
dirName, fileName = os.path.split(os.path.abspath(sys.argv[0]))
filePath = os.path.join(dirName, "p079_keylog.txt")
fileContent = open(filePath, "r")
keyLogs = fileContent.read()
fileContent.close()

#divides the input by lines
keyLogListString = keyLogs.split("\n")
#removes all duplicates
keyLogListString = list(dict.fromkeys(keyLogListString))

uniqueValuesWitOccurances = {}

#put the file input into dictionary where key is one number and value is list of key logs where the key is present
for keyLog in keyLogListString:
    listOfKeyLogs = []
    if keyLog:
        charackterList = []
        for char in keyLog:
            char = int(char)
            charackterList.append(char)
            listOfKeyLogs.append(char)

        for value in charackterList:
            if uniqueValuesWitOccurances.keys().__contains__(value):
                uniqueValuesWitOccurances[value].append(listOfKeyLogs)
            else:
                uniqueValuesWitOccurances[value] = [listOfKeyLogs]

#function to get numbers that are lower than the pivot and belongs to a certain set
def getLowerNumber(pivot, setAcceptedNumbers):
    lowerNmbrs = []
    for keyLog in uniqueValuesWitOccurances.get(pivot):
        position = keyLog.index(pivot)
        for x in keyLog:
            if keyLog.index(x) < position and not lowerNmbrs.__contains__(x) and setAcceptedNumbers.__contains__(x):
                lowerNmbrs.append(x)
    return lowerNmbrs

#function to get numbers that are higher than the pivot number and belongs to certain set
def getHigherNumbers(pivot, setAcceptedNumbers):
    higherNmbrs = []
    for keyLog in uniqueValuesWitOccurances.get(pivot):
        position = keyLog.index(pivot)
        for x in keyLog:
            if keyLog.index(x) > position and not higherNmbrs.__contains__(x) and setAcceptedNumbers.__contains__(x):
                higherNmbrs.append(x)
    return higherNmbrs

#initialization of password list
password = [None]* len(uniqueValuesWitOccurances.keys())

# sets the value of pivot number
pivotPosition = int(len(uniqueValuesWitOccurances.keys()) / 2 - 1)
pivot = list(uniqueValuesWitOccurances.keys())[pivotPosition]

#finds the lower numbers and higher numbers from pivot number
lowerNmbrs = getLowerNumber(pivot, uniqueValuesWitOccurances.keys())
higherNmbrs = getHigherNumbers(pivot, uniqueValuesWitOccurances.keys())

#inserts the number in to password set in proper order for numbers lower than pivot
for number in lowerNmbrs:
    lower = getLowerNumber(number, lowerNmbrs)
    higher = getHigherNumbers(number, lowerNmbrs)
    if (len(lower) + len(higher) + 1) == len(lowerNmbrs):
        password[len(lower)] = number

#inserts the number in to password set in proper order for numbers higher than pivot
for number in higherNmbrs:
    lower = getLowerNumber(number, higherNmbrs)
    higher = getHigherNumbers(number, higherNmbrs)
    if (len(lower) + len(higher) + 1) == len(higherNmbrs):
        password[len(lower) + len(lowerNmbrs)+1] = number

#inserts pivot_number on proper position
password[password.index(None)] = pivot
print("The password is ", password)