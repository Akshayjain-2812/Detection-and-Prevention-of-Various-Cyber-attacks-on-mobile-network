################### Generating RAND

# Generate 128 bit RAND value

import sys
import uuid

id = uuid.uuid4()
RAND = id.hex  #generate 128 bit hex key
y = int(RAND,16)  #convert hexadecimal value of RAND to decimal value
x = int.bit_length(y) #store the length of key

#Run the loop if the length of RAND is not 128

if (x != 128):
    while True:
        id = uuid.uuid4()
        RAND = id.hex  #generate 128 bit hex key
        y = int(RAND,16)  #convert hexadecimal value of RAND to decimal value
        x = int.bit_length(y) #store the length of key
        if(x == 128):  # stop when length is 128
            break

print("Value of RAND is: " + RAND)
#print("\n")
#print("The value of RAND in bits is ")
#print(x) #check the length of int
#print("\n")


#Splitting RAND
r = int(len(RAND)/2)  #storing half the length = 64 bits
#print(r)
r_left = RAND[:r]  #storing first half
#print("The Left 64 Bits of RAND are: " + r_left)
r_right = RAND[r:]  #stroing second half
#print("The Right 64 Bits of RAND are: " + r_right)
print("\n")

from MOB_STN import k_left, k_right,RES

##################### XOR HEX VALUES
def xor_string(a,b):
    bit = 0
    p = ''
    b1 = bin(int(a,16))[2:]   # coverting value to binary
    #print(b1)
    b2 = bin(int(b,16))[2:]   ## coverting value to binary
    #print(b2)
    for x,y in zip(b1,b2):
        z = (int(x) ^ int(y))  # performing bitwise xor
        s = str(z)
        p = p + s              #storing the value in a string
        bit = bit + 1          #counting the bits
    return(p)
#######################################
lhs_xor = xor_string(r_left,k_right)
rhs_xor = xor_string(r_right,k_left)

#################### XOR BINARY VALUES
def xor(a,b):
    bit = 0
    p = ''
    for x,y in zip(a,b):
        z = (int(x) ^ int(y)) #performing bitwise xor
        s = str(z)
        p = p + s             #storing it in a string
        bit = bit + 1
    #print(bit)
    return(p)


num = xor(lhs_xor,rhs_xor)  # Generating a 64 bit number
#print(num)

d = int(len(num)/2)
num_left = num[:d]          #splitting the number into left 32 bits
num_right = num[d:]         #splitting the number into right 32 bits

SRES = xor(num_left, num_right)  #Generating SRES
print("The SRES generated is: " + SRES)
if RES == SRES:
    print("The response match, A3 successful")
else:
    print("Response do not match, authentication failed")
print("\n")
print("###################### A8 algorithm ##########################")
print("\n")
print("Key generation using A8 algorithm:")
print("\n")
a = int(r_left,16)
b = int(r_right,16)
c = int(k_left,16)
d = int(k_right,16)
 ####bitwise and
e = a & d
f = b & c
g = e | f
####converting result to binary
key = bin(g)
key = key[2:]

print("The 64 bit ciphering key is: ")
print(key)
print("\n")
print("######################### A8 algorithm ###################")
print("\n")
import A5
exit()
