# write a python program to get the length of keys , and values in the dictionary =>
dictionary_of_user_information = {
    "userName" : "Mahmoud Khalid Shabaan Omar",
    "userAge" : "22 Years",
    "userUniversity" : "October 6 University.",
    "userFaculty" : "Computer Science And Information System.",
    "userAddress" : "8 Nassar Nassif Kafr El Gabal El Haram El Giza Egypt."
}
print("The Dictionary Of The User Information Is : ",str(dictionary_of_user_information))
print("The Length Of The Dictionery Of The User Information Is : ",str(len(dictionary_of_user_information))+" Keys With Values.")
print("The Length Of The Keys Of The Dictionary Of The User Information Is = ",str(len(dictionary_of_user_information.keys()))+" Keys")
print("The Length Of The Values Of The Dictionary Of The User Information Is : ",str(len(dictionary_of_user_information.values()))+" Values")