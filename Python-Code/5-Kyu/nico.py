def nico(key, message):
    encrypedMessage = ""
    sortedKey = [character for character in key]
    dictionaryKey = {character:[] for character in key}
    

    counter = 0
    for char in message:
        dictionaryKey[sortedKey[counter]].append(char)
        counter+= 1
        if counter == len(sortedKey):
            counter = 0

    lengthOfString = len(dictionaryKey[sortedKey[0]])
    for key, item in dictionaryKey.items():
        if len(item) != lengthOfString:
            dictionaryKey[key].append(' ')
    
    sortedKey.sort()
    counter = 0
    while (counter != lengthOfString):
        for key in sortedKey:
            encrypedMessage += dictionaryKey[key][counter]
        counter += 1
    return(encrypedMessage)