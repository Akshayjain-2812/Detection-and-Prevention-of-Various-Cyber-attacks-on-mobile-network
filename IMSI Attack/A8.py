import random
import uuid
id1 = uuid.uuid4()
Ki = id1.hex #generate a 128 bit hex string
y = int(Ki,16)     #convert hexadecimal value of Ki to decimal value
z = int.bit_length(y) #no of bits of Ki

#Run the loop if length of Ki is not 128

if (z != 128):
    while True:
        id = uuid.uuid4()
        Ki = id.hex   #generate a new Ki
        y = int(Ki,16)
        z = int.bit_length(y)
        #print(z)
        if(z == 128):
            break
#print("The value of Ki is: " + Ki)
#print("Ki is: " )


id3 = uuid.uuid4()
RAND = id3.hex #generate a 128 bit hex string
y1 = int(RAND,16)     #convert hexadecimal value of Ki to decimal value
z1 = int.bit_length(y1) #no of bits of RAND

#Run the loop if length of RAND is not 128

if (z1 != 128):
    while True:
        id2 = uuid.uuid4()
        RAND = id2.hex   #generate a new RAND
        y1 = int(RAND,16)
        z1 = int.bit_length(y1)
        #print(z)
        if(z1 == 128):
            break
#print("The value of RAND is: " + RAND)
#print("RAND is: " )
#print(RAND)

#Splitting Ki
t = int(len(Ki)/2) #storing half the length = 64 bits
#print(t)
k_left = Ki[:t]   #storing first half
#print("The Left 64 Bits of Ki are: " + k_left)
k_right = Ki[t:]  #stroing second half
#print("The Right 64 bits of Ki are: " + k_right)
#print("\n")

#Splitting RAND
r = int(len(RAND)/2)  #storing half the length = 64 bits
#print(r)
r_left = RAND[:r]  #storing first half
#print("The Left 64 Bits of RAND are: " + r_left)
r_right = RAND[r:]  #stroing second half
#print("The Right 64 Bits of RAND are: " + r_right)
#print("\n")

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
