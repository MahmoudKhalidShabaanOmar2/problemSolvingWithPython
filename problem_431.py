# write a python program to get the extension of the file only that you entered from the user by using function =>
import os
file_name_with_extenstion = input("Please Enter The File Name With File Extenstion Is : ")
def get_file_extenstion(file_name_with_ext):
    print("The File Name With Extenstion Is : ",file_name_with_ext)
    file_name , file_extenstion = os.path.splitext(file_name_with_ext)
    print("The File Extenstion Is : ",file_extenstion)
get_file_extenstion(file_name_with_extenstion)