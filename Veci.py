x = int(input())  # Read the input number 'x'
num = x + 1  # Initialize a variable 'num' to the next number

# Define a function to check if two numbers are anagrams of each other
def anagram(a, b):
    a = list(str(a))  # Convert 'a' to a list of its digits
    b = list(str(b))  # Convert 'b' to a list of its digits
    
    for i in range(len(a)):
        if a[i] not in b:
            return False
        else:
            b.pop(b.index(a[i]))  # Remove the digit from 'b'
    
    return True

while True:
    if len(str(num)) > len(str(x)):
        print(0)  # If 'num' becomes longer than 'x', no anagram is found
        break
    if anagram(num, x):
        print(num)  # If 'num' is an anagram of 'x', print 'num' and exit
        break
    num = num + 1  # Increment 'num' to check the next number
