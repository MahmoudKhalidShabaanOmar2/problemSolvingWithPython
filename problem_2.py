# write a python program to get the file name with extenstion , and then displaying the file name , and file extenstion by using function method =>
import os
file_name_with_extenstion = input("Please Enter The File Name With File Extenstion Is : ")
def get_file_name_with_file_extenstion(file_name_with_ext):
    print("The File Name With File Extenstion Is : ",file_name_with_ext)
    file_name , file_extenstion = os.path.splitext(file_name_with_ext)
    print("The File Name Is : ",file_name)
    print("The File Extenstion Is : ",file_extenstion)
get_file_name_with_file_extenstion(file_name_with_extenstion)