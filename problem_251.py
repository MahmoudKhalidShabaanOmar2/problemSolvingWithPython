# write a python program to get sentence from the user , and then please count specific characters , or specific words in the sentence is : 
sentence = input("please enter the sentence is : ")
print("the sentence is : "+sentence)
specific_word_char = input("please enter the specific word or specific character is : ")
print("the specific character , or specific word is : "+specific_word_char)
total_nums_of_specific_word_char = sentence . count(specific_word_char)
print("the total numbers of the specific word , or specific character is : "+str(total_nums_of_specific_word_char)+" times in the sentence")