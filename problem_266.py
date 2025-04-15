# write a python program to get sentence from the user , then display the last character from the sentence , and at the end display all characters from the sentence by using function => 
sentence = input("Please Enter The Sentence Is : ")
def get_sentence(sen) :
    print("All Characters Of The Sentence Is : "+sen)
    for i in sen :
        print(i)
    last_char_from_sentence = sen[-1]
    print("The Last Character From The Sentence Is : "+last_char_from_sentence)
get_sentence(sentence)