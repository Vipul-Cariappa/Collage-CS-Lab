# match brackets

def check_brackets(string):
    count = 0
    for i in string:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
    
    return not bool(count)


s = input("Enter a string: ")

if check_brackets(s):
    print("Brackets matched")
else:
    print("Brackets not matched")
