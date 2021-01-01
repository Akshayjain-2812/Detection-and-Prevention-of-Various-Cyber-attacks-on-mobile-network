import uuid
from HOME_STN import r_left,r_right  #import RAND generated from HOME_STN
#print(r_left)
#print(r_right)

#Generate 128 bit Ki value

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
print("The value of Ki is: " + Ki)
#print("\n")
#print("Size of Ki in bits is: ")
#print(int.bit_length(y)) #check the length of int
#print("\n")

##########splitting of 128 bits into 64 bits

#Splitting Ki
t = int(len(Ki)/2) #storing half the length = 64 bits
#print(t)
k_left = Ki[:t]   #storing first half
#print("The Left 64 Bits of Key are: " + k_left)
k_right = Ki[t:]  #stroing second half
#print("The Right 64 bits of Key are: " + k_right)
print("\n")


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

RES = xor(num_left, num_right)  #Generating RES
print("The RES generated is: " + RES)
