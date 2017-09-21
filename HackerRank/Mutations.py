def mutate_string(string, position, character):
    newString = list(string)
    newString[position] = character
    string = ''.join(newString)
    return string
