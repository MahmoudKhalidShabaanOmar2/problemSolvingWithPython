# write a python program to store name , address , contact in dictionary and then update his , or her contact number at the running time=>
dictionary_of_user_information = {
    "user_name" : "Mahmoud Khalid Shabaan Omar Sallam" ,
    "user_address" : "8 Nassar Nassif Street Kafr El Gabal El Giza Egypt" ,
    "user_contact_number" : input("please enter the contact number of the user is : ") 
}
print("the dictionary of the user information before updating the contact number of the user at the running time is : "+str(dictionary_of_user_information))
dictionary_of_user_information . update({"user_contact_number" : input("please enter the new contact number of the user is : ")})
print("the dictionary of the user information after updating the contact number of the user at the running time is : "+str(dictionary_of_user_information))