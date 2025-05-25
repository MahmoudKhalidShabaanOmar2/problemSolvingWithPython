# write a python program to get the file name with file extension , and then display the file name , and file extenstion , and at the end check if the file extension is ".mp3" then print this file is not allowed by using function method =>
# import os 
# file_name_with_file_extenstion = input("Please Enter The File Name With The File Extenstion Is : ")
# def getFileNameWithFileExtenstion(name_with_extenstion) :
#     print("The File Name With The File Extenstion Is : ",name_with_extenstion) 
#     file_name , file_extenstion = os.path.splitext(name_with_extenstion)
#     print("The File Name Is : ",file_name)
#     print("The File Extenstion Is : ",file_extenstion)
#     if(file_extenstion == ".mp3") :
#         print("This File Is Not Allowed , Because The File Extenstion Is : ",file_extenstion)
#     else :
#         print("This File Is Allowed Because The File Extentsion Is : ",file_extenstion)
# getFileNameWithFileExtenstion(file_name_with_file_extenstion)

import os 
def getFileNameWithFileExtenstion(name_with_extenstion) :
    print("The File Name With The File Extenstion Is : ",name_with_extenstion)
    file_name , file_extenstion = os.path.splitext(name_with_extenstion)
    print("The File Name Is : ",file_name)
    print("The File Extenstion Is : ",file_extenstion)
    if(file_extenstion == ".mp3") :
        return "This File Is Not Allowed"
    else :
        return "This File Is Allowed"
file_name_with_file_extenstion = input("Please Enter The File Name With The File Extenstion Is : ")
checking_file_extenstion = getFileNameWithFileExtenstion(file_name_with_file_extenstion)
print(checking_file_extenstion)