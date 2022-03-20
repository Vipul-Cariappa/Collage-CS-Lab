# reverse a string, and find it is palindrome

def reverse(string):
    reversed_string = ""
    for i in string:
        reversed_string = i + reversed_string
    
    return reversed_string


string = input("Enter a string: ")
reversed_string = reverse(string)

if string == reversed_string:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome ")
