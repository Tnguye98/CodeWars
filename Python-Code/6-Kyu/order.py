def order(sentence):
    sentenceList = sentence.split()
    sentenceOrdered = ""
    count = 1
    while count != len(sentenceList) + 1:
        for word in sentenceList:
            for character in word:
                if character == str(count):
                    sentenceOrdered += word
                    break
        if count != len(sentenceList):
            sentenceOrdered += " "
        count += 1
    return sentenceOrdered



print(order("4of Fo1r pe6ople g3ood th5e the2"))