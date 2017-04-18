def convertToReversePolish(expression):
    splited_expression = list(str(expression))
    opr_list = []
    reverse = []

    for char in splited_expression:
        if char == "+" or char == "-" or char == "*" \
                or char == "/" or char == "^":
            opr_list.append(char)
        
        if char.isalpha():
            reverse.append(char)
            
        if char == ")":
            reverse.append(opr_list.pop())
            
    
    return "".join(reverse)

def main():
    expression_list = []
    reverse_list = []
    
    opt = input()

    if opt == "test":
        expression_list = [3, "(a+(b*c))", "((a+b)*(z+x))", "((a+t)*((b+(a+c))^(c+d)))"]
        num_expression = -1
    else:
        num_expression = int(opt)
    
    if not num_expression == -1:
        for idx in range(num_expression):
            expression_list.append(input())

    for idy, expression in enumerate(expression_list):
        reverse_list.append(
            convertToReversePolish(expression))
            
        if reverse_list[idy]:
            print(reverse_list[idy])
        
main()
