list1={}
user_in=input("Enter your Password : ")
print(user_in)
check=False

for digit in user_in:
    if digit.isdigit():
     check=True
list1["Has digits"]=check

check1=False
for digit in user_in:
    if digit.isupper():
     check1=True
list1["Captial"]=check1

check3=0          
if user_in.__len__()>=8 :
    check3=True
    list1["Number of values"]=check3
else:
    check3=False
    
    list1["Number of values"]=check3
print(list1)

if all(list1.values()):
    print("Password is strong")
else:
    print("Weak password")    
    