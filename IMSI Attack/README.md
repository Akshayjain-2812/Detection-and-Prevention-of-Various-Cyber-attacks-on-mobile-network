Download the android emulator for simulated mobile environment (https://developer.android.com/studio/run/emulator) After successfully downloading the emulator, follow the following steps:

Steps for extracting gsm data from emulator:

open cmd as admin.
goto android-sdk platforms
emulator -avd Nexus_5X_API_29_x86
open another cmd as admin
goto android-sdk platform tools
adb logcat -e CellIdentityGsm > logcat.txt
extract imsi number:

open cmd
got android-sdk platform-tools
adb shell service call iphonesubinfo 7 ---- imsi
adb shell service call iphonesubinfo 1 ---- imei
adb shell service call iphonesubinfo 10 ---- iccid
adb shell service call iphonesubinfo 12 ---- phone number.
Store the extracted files in a text file in the same directory as your python file

Download all the files containing details of cell towers of different locations from https://drive.google.com/drive/folders/1Zl6jKckItoKf4j39KPxZPhIJQMKkihGU

Create a new csv file containing only the Loaction id and summation of cell tower id for the specific location - add1.csv

Execute the imsi.py file The explanation of the code is written in the file
