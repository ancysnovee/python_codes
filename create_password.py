#Program to create passwords:

import random
an="ABC"
i=0
while i<=10:
     name=input("enter your name: ")
     if len(name)>2:
          slic=name[:3]
          low=slic.lower()
          a=(f"YOUR PASSWORD IS: {an}{low}{random.randint(100000,999999)}")
          print(a)
          i+=1
     else:
         print("name should be more than 3 characters")
               
print("stop")

