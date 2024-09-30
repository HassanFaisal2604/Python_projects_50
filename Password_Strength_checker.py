user_in = input("Enter your Password : ")
print(user_in)

list1 = {
    "Has digits": any(digit.isdigit() for digit in user_in),
    "Captial": any(digit.isupper() for digit in user_in),
    "Number of values": len(user_in) >= 8
}

print(list1)

if all(list1.values()):
    print("Password is strong")
else:
    print("Weak password")    