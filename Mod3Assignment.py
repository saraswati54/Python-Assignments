#2ndANS
 
# Function to calculate x
# raised to the power y
def power(x, y):
 
    if (y == 0): return 1
    elif (int(y % 2) == 0):
        return (power(x, int(y / 2)) *
               power(x, int(y / 2)))
    else:
        return (x * power(x, int(y / 2)) *
                   power(x, int(y / 2)))
 
# Driver Code
x = 2; y = 3
print(power(x, y))

#3rdANS

mylist = [["john", 1, "a"], ["larry", 0, "c"]]

#print("Sorted based on name: %s" % sorted(mylist, key=lambda l: l[0]))
print("Sorted based on second element(0/1): %s" % sorted(mylist, key=lambda l: l[1]))
#print("Sorted based on third element(a/b): %s" % sorted(mylist, key=lambda l: l[2]))
#print("-" * 77)


#4thANS

#Sort the list using operator.itemgetter function 
#mylist = [["john", 1, "a"], ["larry", 0, "b"]]. Sort the list by second item 1 and 0

mylist = [["john", 1, "a"], ["larry", 0, "b"]]
from operator import itemgetter
print(sorted(mylist, key=itemgetter(1)))