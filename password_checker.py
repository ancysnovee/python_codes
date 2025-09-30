#Program to check if the password is accepted:

password=input("enter your password")
special_chars = {"@", "#", "$", "&"}
true=0
if len(password)>12 and len(password)<=64:
   for char in password:
       if char in special_chars:
           true=1
           break
   if true==1:
       if password.isalpha() or password.isdigit():
           print("Password should include both characters and numbers.")
       else:
           print("Password is accepted.")
   else:
       print("Password must include at least one special character (@, #, $, &).")
else:
   print("password must be at least 12 char long")
