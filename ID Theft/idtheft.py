import hashlib
fo = open("sharockyou.txt", "r")
file_contents = fo.read()
val = input("Enter your value: ")
#print(val)
result = hashlib.sha256(val.encode())
#print(result.hexdigest())
test = result.hexdigest()
Flag = 0
for i in file_contents.split('\n'):
    if test == i:
        Flag = 1
if Flag == 1:
    print("Leaked password")
else:
    print("Password is not leaked")
