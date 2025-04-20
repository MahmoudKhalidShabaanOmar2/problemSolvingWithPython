# write a python program to get sentence from the user , the system should display only ten characters maximum => 
s_sentence = input("Please Enter The String Sentence Is : ")
print("The Sentence Is : "+s_sentence)
removed_chars_words = input("Please Enter The Removed Chars , Or Removed Words Is : ")
print("The Removed Characters , Or Removed Words Is : "+removed_chars_words)
updated_s_sentence = s_sentence . replace(removed_chars_words , "")
print("The Updated String Sentence Is : "+updated_s_sentence)