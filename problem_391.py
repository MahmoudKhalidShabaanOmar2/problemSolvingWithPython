# write a python program to get the file name with the file extension , and then check if the file extension is ".mp3" , Then print this file is not allowed =>
import os 
file_name_with_file_extension = input("Please Enter The File Name With The File Extenstion Is : ")
print("The File Name With The File Extenstion Is : ",file_name_with_file_extension)
file_name , file_extension = os.path.splitext(file_name_with_file_extension)
print("The File Name Is : ",file_name)
print("The File Extension Is : ",file_extension)
if(file_extension == ".mp3") :
    print("This File Is Not Allowed , Because The File Extension Is : ",file_extension)
else :
    print("This File Is Allowed , Because The File Extension Is : ",file_extension)