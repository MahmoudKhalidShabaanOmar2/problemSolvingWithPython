# write a python program to get user biography description , and then count the total character , and length of specific words of the user description biography =>
user_biography_description = input("please enter the user biography description is : ")
print("the user biography description is : \""+user_biography_description+"\"")
print("the total characters of the user biography description is = "+str(len(user_biography_description))+" characters")
user_biography_description_lista = user_biography_description . split()
print("the user biography description list is = "+str(user_biography_description_lista))
print("the length of the specific words in the user biography description list is = "+str(len(user_biography_description_lista))+" specific words")