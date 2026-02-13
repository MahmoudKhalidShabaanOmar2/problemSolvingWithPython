# write a returned function to get the file name with file extension , and then check if the file extension is .mp3 , if the file extension is not .mp3 , then print the file with mp3 extension is not allowed by using function method =>
import os 
def check_file_extension(file_name_with_file_extension):
    print("The File Name With The File Extension Is : ",file_name_with_file_extension)
    file_name , file_extension = os.path.splitext(file_name_with_file_extension)
    print("The File Name Is : ",file_name)
    print("The File Extension Is : ",file_extension)
    if(file_extension == ".mp3"):
        return (f"This File Extension Is Not Allowed , Because The File Extension Is : "+file_extension)
    else:
        return (f"This File Extension Is Allowed , Because The File Extension Is : "+file_extension)
file_name_with_file_extension = input("Please Enter The File Name With File Extension Is : ")
check_file_name_with_file_extension = check_file_extension(file_name_with_file_extension)
print(check_file_name_with_file_extension)