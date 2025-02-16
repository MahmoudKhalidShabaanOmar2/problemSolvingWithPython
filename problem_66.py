# write a python program to get a character from the user , and then check character wether vowel , consonant , or numeric character =>
# character = input("please enter the character is : ")
# print("the character is : \""+character+"\"")
# if((character == "A") or (character == "a")) :
#     print("it is a vowel character , because your entered character is : \""+character+"\"")
# elif((character == "E") or (character == "e")) :
#     print("it is a vowel character , because your entered character is : \""+character+"\"")
# elif((character == "I") or (character == "i")) :
#     print("it is a vowel character , because your entered character is : \""+character+"\"")
# elif((character == "O") or (character == "o")) :
#     print("it is a vowel character , because your entered character is : \""+character+"\"")
# elif((character == "U") or (character == "u")) :
#     print("it is a vowel character , because your entered character is : \""+character+"\"")
# elif(character . isnumeric()) :
#     print("it is a numeric character , because your entered character is : \""+character+"\"")
# else :
#     print("it is a consonant character , because your entered character is : \""+character+"\"")

character = input("please enter the character is : ")
print("the character is : \""+character+"\"")
if(((character == "A") or (character == "a")) or ((character == "E") or (character == "e")) or ((character == "I") or (character == "i")) or ((character == "O") or (character == "o")) or ((character == "U") or (character == "u"))) :
    print("it is a vowel character , because your entered character is : \""+character+"\"")
elif(character . isnumeric()) :
    print("it is a numeric character , because your entered character is : \""+character+"\"")
else :
    print("it is a consonant character , because your entered character is : \""+character+"\"")