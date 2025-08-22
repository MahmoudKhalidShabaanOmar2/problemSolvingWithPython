# write a python program to get the file name with file extenstion , and then check if the file extenstion is ".mp3" displaying this file is not allowed , please enter new file extenstion by using function method =>
import os
file_name_with_extenstion = input("Please Enter The File Name With File Extenstion Is : ")
def check_file_extenstion(file_name_with_ext):
    print("The File Name With File Extenstion Is : ",file_name_with_ext)
    file_name , file_extenstion = os.path.splitext(file_name_with_ext)
    print("The File Name Is : ",file_name)
    print("The File Extenstion Is : ",file_extenstion)
    if(file_extenstion == ".mp3"):
        print("This File Is Not Allowed , Please Enter New File Extenstion")
    else:
        print("This File Is Allowed")
check_file_extenstion(file_name_with_extenstion)