# write a python prorgram to search any character (or set of characters) from a string =>
s_sentence = input("Please Enter The String Sentence Is : ")
print("The String Sentence Is : "+s_sentence)
s_characters = input("Please Enter The Set Of Characters , Or Characters Is : ")
print("The Set Of Characters , Or Characters Is : "+s_characters)
if(s_characters in s_sentence) :
    print("The Set Of Characters , Or Characters Is Exisiting In String Sentence")
else :
    print("The Set Of Characters , Or Characters Is Not Exisiting In String Sentence")