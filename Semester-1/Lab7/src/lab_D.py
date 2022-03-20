# program function that takes a list of integer 
# and returns True if the absolute difference between each adjacent pair of elements strictly increases

def check_increases(array):
    previous = abs(array[1] - array[0])

    for i in range(len(array)-1):
        new = abs(array[i+1] - array[i])
        if previous > new:
            return False
        previous = new
    
    return True

l = list(map(int, input("Enter list of intergers: ").split()))

if check_increases(l):
    print("It is increasing")
else:
    print("It is not increasing")
