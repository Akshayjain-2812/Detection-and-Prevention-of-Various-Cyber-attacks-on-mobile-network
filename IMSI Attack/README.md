Download the android emulator for simulated mobile environment (https://developer.android.com/studio/run/emulator)
After successfully downloading the emulator, follow the following steps:

Steps for extracting gsm data from emulator:
1. open cmd as admin.
2. goto android-sdk platforms
3. emulator -avd Nexus_5X_API_29_x86
4. open another cmd as admin
5. goto android-sdk platform tools
6. adb logcat -e CellIdentityGsm > logcat.txt

extract imsi number:
1. open cmd 
2. got android-sdk platform-tools
3. adb shell service call iphonesubinfo 7 ---- imsi
4. adb shell service call iphonesubinfo 1 ---- imei
5. adb shell service call iphonesubinfo 10 ---- iccid
6. adb shell service call iphonesubinfo 12 ---- phone number.

Store the extracted files in a text file in the same directory as your python file

Download all the files containing details of cell towers of different locations from https://drive.google.com/drive/folders/1Zl6jKckItoKf4j39KPxZPhIJQMKkihGU
 
Create a new csv file containing only the Loaction id and summation of cell tower id for the specific location - add1.csv

Execute the imsi.py file
The explanation of the code is written in the file
