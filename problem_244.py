# write a python prorgram to get sentence from the user , and then calculate the specific words , or characters on that sentence by using function => 
sentence = input("please enter the sentence is : ")
specific_word_char = input("please enter the specific words , or specific characters is : ")
def get_total_specific_words_chars(sen , spec_w_c) :
    print("the sentence is : \""+sen+"\"")
    print("the specific words , or specific characters is : \""+spec_w_c+"\"")
    total_nums_of_specific_words_chars = sen . count(spec_w_c)
    print("the total numbers of the specific words or specific characters is : "+str(total_nums_of_specific_words_chars)+" times in the sentence")
get_total_specific_words_chars(sentence , specific_word_char)