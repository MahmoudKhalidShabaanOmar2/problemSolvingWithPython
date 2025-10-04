# write a python program to get file name with extenstion , and then displaying the file extenstion only =>
import os 
file_name_with_file_extenstion = input("Please Enter The File Name With File Extenstion Is : ")
print("The File Name With The File Extenstion Is : ",file_name_with_file_extenstion)
file_name , file_extenstion = os.path.splitext(file_name_with_file_extenstion)
print("The File Name Is : ",file_name)
print("The File Extenstion Is :"+file_extenstion)