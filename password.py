import random 
import string 
pass_len = 8
password = string.ascii_letters + string.digits + ("_@#")

pas = " "
for i in range (pass_len):
    pas += random.choice(password)

print("Your Random Password is :- ", pas)