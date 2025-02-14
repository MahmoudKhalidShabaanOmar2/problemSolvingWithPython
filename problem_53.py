# write a python program to store name , address , contact in dictionary and then update his , or her contact number =>
dictionary_of_user_information = {
    "user_name" : "Mahmoud Khalid Shabaan Omar Sallam" ,
    "user_address" : "8 Nassar Nassif Street Kafr El Gabal El Haram El Giza Egypt" ,
    "user_contact_number" : "01062936323" 
}
print("the dictionary of the user information is : "+str(dictionary_of_user_information))
dictionary_of_user_information . update({"user_contact_number" : "01111563232"})
print("the dictionary of the user information after updating the contact number of the user is : "+str(dictionary_of_user_information))