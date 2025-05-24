# write a python program to get any file with extension , to display only that file name , and file extension =>
import os 
file_name_with_file_extension = input("Please Enter The File Name With File Extension Is : ")
print("The File Name With The File Extension Is : ",file_name_with_file_extension)
file_name , file_extension = os.path.splitext(file_name_with_file_extension)
print("The File Name Is : ",file_name)
print("The File Extension Is : ",file_extension)