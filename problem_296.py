# write a python program to get string sentence from the user , the system should display all characters except last ten characters => 
s_sentence = input("Please Enter The String Sentence Is : ")
print("The String Sentence Is : "+s_sentence)
sentence_after_removing_last_10chars = s_sentence[:-10]
print("The Sentence After Removing The Last Ten Characters Is : "+sentence_after_removing_last_10chars)