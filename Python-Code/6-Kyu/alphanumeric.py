def alphanumeric(password):
    if len(password) == 0:
        return False

    flag = 0
    for character in password:
        asciiValue = ord(character)
        if 48 <= asciiValue <= 57 or 65 <= asciiValue <= 90 or 97 <= asciiValue <= 122:
            continue
        else:
            flag = 1
    if flag == 1:
        return False
    return True 

print(alphanumeric("HELLOworld123"))