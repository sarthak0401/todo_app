password = input("Enter the password: ")
res = {}
# 1 : length >=8
# 2 : One upper case letter
# 3 : One numeric character

if len(password) >=8:
    res["Length"] = True
else:
    res["Length"] = False


res['UpperCase'] = False
for i in password:
    if i.isupper():
        res['UpperCase'] = True
            

res["Digit"] = False
for i in password:
    if i.isdigit():
        res["Digit"]= True 



print(res.values())

# print(all(res.values()))
if all(res.values()):
    print("Strong password")
else:
    print("Weak password")

# isupper () -> this checks for the individual characters
# upper() -> makes the string in upper case
