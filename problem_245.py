# write a python program to get sentence from the user , and then calculate the specific characters , or specific words , and then replace the specific characters , or specific words by using function method =>
sentence = input("please enter the sentence is : ")
specific_word_char = input("please enter the specific word , or specific character is : ")
replacement_word_char = input("please enter the replacement word , or replacement characters is : ")
def get_sentence(sen , spec_w_c , repla_w_c) :
    print("The Sentence Is : \""+sen+"\"")
    print("The Specific Word Or Specific Character Is : \""+spec_w_c+"\"")
    total_nums_of_spec_w_c = sentence . count(spec_w_c) 
    print("The Total Numbers Of The Specific Words , Or Specific Characters Is = "+str(total_nums_of_spec_w_c)+" times")
    print("The Replacement Specific Word , Or Specific Character Is : \""+repla_w_c+"\"")
    replacement_sentence = sentence . replace(spec_w_c , repla_w_c) 
    print("The Replacement Sentence Is : \""+replacement_sentence+"\"")
get_sentence(sentence , specific_word_char , replacement_word_char)