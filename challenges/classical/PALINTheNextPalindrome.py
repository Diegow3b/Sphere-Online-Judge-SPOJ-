def findNextPalindrome(number):
    new_list = []
    list_number = list(str(number))
    
    size = len(list_number)
    first = list_number[0]
    last = list_number[size-1]
    
    if first == last and size == 3:
        new_list = list_number
        new_list[1] = str(int(list_number[1]) + 1)
    elif size > 3:
        for i in range(size):
            if i == 0 or i == size-1:
                new_list.append(list_number[0])
            else:
                if list_number[1] == 9:
                    str(int(list_number[1-1]) + 1 )
                new_list.append(str(int(list_number[1])+1))
    
    result = int(''.join(new_list))
    
    return result

def main():
    result_list = []
    amount = int(input())

    for i in range(amount):
        result_list.append(findNextPalindrome(int(input())))
        
    for result in result_list:
        print(result)

main()
