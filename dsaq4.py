#  program to print the first non-repeated character from a string.
NO_OF_CHARS = 256

def getCharCountArray(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)]+= 1
    return count

def firstNonRepeating(string):
    count = getCharCountArray(string)
    index = -1
    l = 0

    for i in string:
        if count[ord(i)] == 1:
            index = l
            break
        l += 1

    return index

string = "Edyoda"
index = firstNonRepeating(string)
if index == 1:
    print ("String is empty")
else:
    print ("1st non-repeating character is: " + string[index])