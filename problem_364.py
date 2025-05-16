# write a python program to get string sentence from the user , and the sentence should be able to remove a word from the sentence by using function method =>
sentence = input("Please Enter The Sentence Is : ")
replacement_word = input("Please Enter The Replacement Word Is : ")
removed_word = input("Please Enter The Removed Word Is : ")
def get_string_sentence(sen , repla_sen , remov_sen) :
    print("The String Sentence Is : ",sen)
    print("The Replacement Sentence Is : ",repla_sen)
    print("The REmoved Sentence Is : ",remov_sen)
    updated_sentence = sen . replace(remov_sen , repla_sen)
    print("The Updated String Sentence Is : ",updated_sentence)
get_string_sentence(sentence , replacement_word , removed_word)