# write a python program to checck the file extenstion of a file , if the file extenstion is ".mp3" then displaying a message , "this file is not allowed" =>
import os
file_name_with_file_extenstion = input("Please Enter The File Name With File Extenstion Is : ")
print("The File Name With File Extenstion Is : ",file_name_with_file_extenstion)
file_name , file_extenstion = os.path.splitext(file_name_with_file_extenstion)
print("The File Name Is : ",file_name)
print("The File Extenstion Is : ",file_extenstion)
print("Check If The File Extenstion Allowed , Or Not Allowed : ")
if(file_extenstion == ".mp3"): 
    print("The File Extenstion Is Not Allowed")
else:
    print("The File Extenstion Is Allowed")