# write a python program to get a sentence from the user to find occurrence of a specific words or characters in a sentence , then replace with another word or character =>
sentence = input("please enter the sentence is : ")
print("the sentence is : "+sentence)
specific_word_char = input("please enter the specific word , or character is : ")
print("the specific word , or specific character is : "+specific_word_char)
total_nums_of_specific_words_chars = sentence . count(specific_word_char)
print("the total numbers of the specific words , or specific characters is : "+str(total_nums_of_specific_words_chars)+"times")
replacement_word_char = input("please enter the replacement word , or characters is : ")
print("the replacement character or word is : "+replacement_word_char)
replacement_sentence = sentence . replace(specific_word_char , replacement_word_char)
print("the replacement sentence is : "+replacement_sentence)