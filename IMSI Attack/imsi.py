#final imsi attack
import os
import re
import csv
import pandas as pd
mylines=[]
str= "mLac" #substring to find.
words=[]
myfile = open(r"C:\android-sdk\platform-tools\logcat.txt","r") #open file where gsm and imsi details is stored
for line in myfile:
    mylines.append(line.rstrip('\n')) #append each line into array
words=(mylines[2])  #store the first entry of data as the rest of data is repititve
#print(words)        #check the data stored
#print('\n')
list=(words.split()) #store the data as a list
#find the required substring from the list
for x in list:
    if x.startswith(str):
        lac = x
print("Current loacation id is  " + lac) #print the current loation id
print('\n')
lacval=int(lac.split("=")[1])  #extract the integer value and store it
#print(lacval)  #test case

##### store specific cell id sum for the location id
data=[]
with open(r"C:\python\2.csv","r") as a:
    reader=csv.reader(a)
    data=([row for row in csv.reader(a)]) #store each row and column value in a list
length=(len(data)) #store the length of list
for x in range(1,length):
    for y in range(0,2):
        data[x][y] = int(data[x][y]) #data in csv file must be in number format
    #print(data[x][0]) #display first column i.e location id of each row... for cell-id-sum change 0 to 1
for x in range(1,length):
    if (data[x][0] == lacval):
        cidsum=(data[x][1]) # store the sum of cell id fo that specific location id
print("The sum of cell id for current Lac is: " )
print(cidsum)
print('\n')

########## Extracting the imsi number of the cell phone
import re
string=""
str=""
text=[]
file = open(r"C:\android-sdk\platform-tools\imsi.txt","r")  #open imsi tet file.
for lines in file:
    text.append(lines.rstrip('\n'))  #store the text in the form of list
#print(text)
for elements in text:
    string+=elements   #store the elements of list into a single string
#print(string)
string = (re.findall("'(.*?)'",string))  #extract the numbers within quotes and it is stored in list format
for e in string :
    str+=e                       #storing the list as a single string
#print(str)
x=[int(s) for s in str.split(".") if s.isdigit()] # extracting only the digits from list
#print(x)
imsi = sum(d * 10**i for i, d in enumerate(x[::-1])) #convert the list into a single integer
print("The IMSI number of the phone is")  # final imsi
print(imsi)
print("\n")
'''
##########################new datat set##############################
print("Scenario 1: ")
data=[]
with open(r"C:\python\add1.csv","r") as a:
    reader=csv.reader(a)
    data=([row for row in csv.reader(a)]) #store each row and column value in a list
length=(len(data)) #store the length of list
for x in range(1,length):
    for y in range(0,2):
        data[x][y] = int(data[x][y]) #data in csv file must be in number format
    #print(data[x][0]) #display first column i.e location id of each row... for cell-id-sum change 0 to 1
for x in range(1,length):
    if (data[x][0] == lacval):
        cidsum1=(data[x][1]) # store the sum of cell id fo that specific location id
print("The updated sum of cell id for current Lac is: " )
print(cidsum1)
print('\n')
######################case 1#########################################
if(cidsum != cidsum1):
    print("The sum of cell id doesn't match")
    print("Since the sum of cell id does not match, there is a possibility of intruder. Hence, further authentication is terminated.")
print("\n")
'''
#################case 2 ###############################################
print("Scenario 2: ")
cidsum2 = cidsum
print("Updated Cell location sum is: ")
print(cidsum2)
print("\n")
if(cidsum2 == cidsum):
    print("The sum of Cell Id's match.")
print("\n")
print("################### GSM authentication ###############")
print("\n")
print("###################### A3 algorithm ###################")
print("\n")
import HOME_STN #Start with GSM authentication
