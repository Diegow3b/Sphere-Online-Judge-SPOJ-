# I'm not sure if this is 100% correct
def substringCheck(subString):
    string = subString.split(' ')
    stringA = string[0]
    stringB = string[1]
    
    if stringB == 0:
        raise ValueError('Second value cant be None')
            
    if not len(stringA) == 10:
        raise ValueError('Invalid size of first sequence, exemple: 1010101010')
        
    if not len(stringB) == 5:
        raise ValueError('Invalid size of second sequence, exemple: 11100')
    
    result = 1 if stringB in stringA else 0
    print result    
    
substringCheck(raw_input())
