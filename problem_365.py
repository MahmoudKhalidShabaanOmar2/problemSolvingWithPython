# write a python program to get sentence from the user , and the system should display only ten characters from the sentence by using function method =>
sentence = input("Please Enter The Sentence Is : ")
def get_string_sentence(sen) :
    print("The Sentence Is : ",sen)
    only_10_chars_from_sentence = sen[:10]
    print("The Ten Characters From The Sentence Only Is : ",only_10_chars_from_sentence)
    if(len(sen) <= 10) :
        print("The Ten Characters From The Sentence Is : ",only_10_chars_from_sentence)
    else :
        print("The Completed Sentence Is : ",sen)
get_string_sentence(sentence)