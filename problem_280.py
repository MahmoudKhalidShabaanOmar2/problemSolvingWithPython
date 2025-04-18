# write a python program to get word from the user , and then remove the frist character from the word , and then remove the last character from the word =>
word = input("Please Enter The Word Is : ")
print("The Word Is : ",word)
frist_char_from_word = word[0]
print("The Frist Character From The Word Is : "+frist_char_from_word)
remove_frist_char_from_word = word[1:]
print("The Word After Removing The Frist Character Is : "+remove_frist_char_from_word)
last_char_from_word = word[-1]
print("The Last Character From The Word Is : "+last_char_from_word)
remove_last_char_from_word = word[:-1]
print("The Word After Removing The Last Character Is : "+remove_last_char_from_word)