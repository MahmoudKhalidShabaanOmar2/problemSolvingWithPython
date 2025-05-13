# write a python program to get a string sentence from the user , and then search in the string sentence by using function method =>
# string_sentence = input("Please Enter The String Sentence Is : ")
# string_characters = input("Please Enter The String Characters Is : ")
# def get_string_sentence(s_sen , s_char) :
#     print("The String Sentence Is : ",s_sen)
#     print("The String Characters Is : ",s_char)
#     if(s_char in s_sen) :
#         print("The String Character Is Existing In The String Sentence")
#     else :
#         print("The String Character Is Not Existing In The String Sentence")
# get_string_sentence(string_sentence , string_characters)

def get_string_sentence(s_sen , s_char) :
    print("The String Sentence Is : ",s_sen)
    print("The String Character Is : ",s_char)
    if(s_char in s_sen) :
        return("The String Character Is Existing In The String Sentence")
    else :
        return("The String Character Is Not Existing In The String Sentence")
string_sentence = input("Please Enter The String Sentence Is : ")    
string_character = input("Please Enter The String Character Is : ")
search_into_string_sentence = get_string_sentence(string_sentence , string_character)
print(search_into_string_sentence)