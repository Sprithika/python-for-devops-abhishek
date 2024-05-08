import sys

var = sys.argv[1]

if var == 't2.micro':
    print("This costs 2$ per day")
elif var == 't2.macro':
    print("This costs 4$ per day")
elif var == 't2.medium':
    print("This costs 6$ per day")
else:
    print("provide correct input")
