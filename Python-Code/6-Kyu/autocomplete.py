def autocomplete(input_, dictionary):
    _input = ''.join([x for x in input_ if x.isalpha()])
    matches = []
    
    for word in dictionary:
        if word.lower().startswith(_input.lower()):
            matches.append(word)
        if len(matches) >= 5:
            break
    return matches


print(autocomplete('ai', ['airplane','airport','apple','ball']))