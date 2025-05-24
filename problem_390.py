# write a python program to get file name with the file extension from the user , and then display the file name , and file extension by using function method =>
import os 
file_name_with_file_extension = input("Please Enter The File Name With File Extension Is : ")
def get_file_name_file_extension(file_name_extension) :
    print("The File Name With File Extenstion Is : ",file_name_extension)
    file_name , file_extension = os.path.splitext(file_name_extension)
    print("The File Name Is : ",file_name)
    print("The File Extension Is : ",file_extension)
get_file_name_file_extension(file_name_with_file_extension)