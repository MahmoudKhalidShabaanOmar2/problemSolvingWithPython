# write a python program to calculate a specific words , or characters in a sentence =>
sentence = input("please enter the sentence is : ")
print("the sentence is : \""+sentence+"\"")
char_word = input("please enter the character , or word is : ")
print("the specific character , or specific word is : \""+char_word+"\"")
total_num_of_specific_w_c = sentence . count(char_word)
print("the total times of the specific character , or specific word is = "+str(total_num_of_specific_w_c)+" times")
print(str(total_num_of_specific_w_c)+" times of \""+char_word+"\" in the presented sentence is : \""+sentence+"\"")