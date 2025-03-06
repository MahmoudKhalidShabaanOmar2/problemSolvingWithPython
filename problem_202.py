# write a python program to get user biography from the user , and then count total characters , and total word in the user biography descrription by using diffferent function methods =>
# user_biography_description = input("please enter the user biography description is : ")
# def get_user_biography_description(user_bio_desc) :
#     print("the user biography description is : \""+user_bio_desc+"\"")
#     print("the total characters of the user biography description is = \""+str(len(user_bio_desc))+"\"")
#     user_bio_desc_lista = user_bio_desc . split()
#     print("the list of the user biography description is = "+str(user_bio_desc_lista))
#     print("the length of the words of the user biography list is = "+str(len(user_bio_desc_lista))+" words")
# get_user_biography_description(user_biography_description)

def get_user_biography_description(user_bio_desc) :
    print("the user biography description is : \""+user_bio_desc+"\"")
    print("the total characters of the user biography description is = \""+str(len(user_bio_desc))+" characters\"")
    user_bio_desc_lista = user_bio_desc . split()
    print("the list of the user biography description is = "+str(user_bio_desc_lista))
    return("the length of the words of the user biography description is = "+str(len(user_bio_desc_lista))+" words")
user_biography_description = input("please enter the user biography description is : ")
bio = get_user_biography_description(user_biography_description)
print(bio)