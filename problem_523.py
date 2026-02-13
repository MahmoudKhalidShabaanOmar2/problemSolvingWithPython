# write a function to return the extension of the file by using python language =>
import os
def get_file_extension(file_name_with_file_extension):
    print("The File Name With The File Extension Is : ",file_name_with_file_extension)
    file_name , file_extension = os.path.splitext(file_name_with_file_extension)
    return "The File Name Is : "+file_name+" , And The File Extension Is : "+file_extension
file_name_with_file_extension = input("Please Enter The File Name With The File Extension Is : ")
get_file_name_with_file_extension = get_file_extension(file_name_with_file_extension)
print(get_file_name_with_file_extension)