# write a python program to get string sentence from the user , and then the user should be able to remove any characters , or words from the string sentence =>
s_sentence = input("Please Enter The String Sentence Is : ")
print("The String Sentence Is : "+s_sentence)
removed_character_word = input("Please Enter The Removed Character , Or Removed Word Is : ")
print("The Removed Characters , Or Removed Words Is : "+removed_character_word)
updated_sentence = s_sentence . replace(removed_character_word , "")
print("The Updated String Sentence Is : "+updated_sentence)