# write a python program to get the biography from the user , and count numbers of characters , and words in the biography description =>
user_biography = input("please enter the user biography description is : ")
print("the user biography is : \""+user_biography+"\"")
print("the total characters of the user biography decription is : \""+str(len(user_biography))+" characters\"")
user_biography_lista = user_biography . split()
print("the list of the user biography description is : "+str(user_biography_lista))
print("the length of the list of the user biography is = "+str(len(user_biography_lista))+" words")