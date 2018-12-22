# Comparing strings with integers

count=0

def check(x,y,z):
    
   if x==y or y==z or x==z:
      return True

   else:
      return False

a=input("Enter first parameter: ")
b=input("Enter second parameter: ")
c=input("Enter third parameter: ")

res=check(a,b,c)
print(res)

# Function for type casting char to int

def check2(x,y,z):
    
   a=int(x)
   b=int(y)
   c=int(z)

   if a==b or b==c or c==a:
      return True

   else:
      return False

res1=check2(7,6,'6')
print(res1)      

# Output: True