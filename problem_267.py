# write a python program to get seentence from the user , and then count the specific characters in the sentence by using different functions methods =>
# sentence = input("Please Enter The Sentence Is : ")
# specific_char_word = input("Please Enter The Specific Word , Or Specific Character Is : ")
# def get_sentence(sen , spec_w_c) :
#     print("The Sentence Is : "+sen)
#     print("The Specific Character , Or Specific Word Is : "+spec_w_c) 
#     total_specific_word_char = sen.count(spec_w_c)
#     print("The Total Specific Words , Or Specific Characters Is = "+str(total_specific_word_char)+" Times In The Sentence")
# get_sentence(sentence , specific_char_word)

def get_sentence(sen , spec_w_c) :
    print("The Sentence Is : "+sen)
    print("The Specific Character , Or Specific Word Is : "+spec_w_c)
    total_specific_word_char = sen . count(spec_w_c)
    return("The Total Specific Words , Or Specific Characters Is = "+str(total_specific_word_char)+" Times In The Sentence")
sentence = input("Please Enter The Sentence Is : ")
specific_word_char = input("Please Enter The Specific Words , Or Specific Characters Is = ")
display_sentence = get_sentence(sentence , specific_word_char)
print(display_sentence)