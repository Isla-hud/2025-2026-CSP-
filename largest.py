#Isla
#Largest
# Write a function with 3 integer parameters (a,b,c) that prints the largest of the three numbers

#Functions
def largest(a,b,c):
    if a>b and a>c:
        print (a)
    if b>a and b>c:
        print(b)
    if c>a and c>b:
        print(c)
#Main
largest(1,2,3)
largest(20,100,10)
largest(100,50,1)
