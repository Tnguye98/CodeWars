def string_transformer(s):
    listString = s.split(" ")[::-1]
    ans = ""
    for word in listString:
        for character in word:
            if ord(character) < 91:
                ans += character.lower()
            else:
                ans += character.upper()
        ans+= " "
    return ans[:-1]


print(string_transformer("Input Example"))