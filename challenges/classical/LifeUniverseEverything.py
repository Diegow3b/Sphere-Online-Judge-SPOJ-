def answerToLife(value):
    while not value == 42:
        print value
        value = int(raw_input())
        
answerToLife(int(raw_input()))
