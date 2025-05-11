# write a python program to get sentence from the user , and then get the frist character , and last character , and then remove the frist character , and last character from the sentence by using function method =>
sentence = input("Please Enter The Sentence Is : ")
def get_sentence(sen) :
    print("The Sentence Is : ",sen)
    frist_character_from_sentence = sen[0]
    print("The Frist Character From The Sentence Is : ",frist_character_from_sentence)
    removing_frist_character_from_sentence = sen[1:]
    print("The Sentence After Removing The Frist Charater Is : ",removing_frist_character_from_sentence)
    last_character_from_sentence = sen[-1]
    print("The Last Character From The Sentence Is : ",last_character_from_sentence)
    removing_last_character_from_sentence = sen[0:-1]
    print("The Sentence After Removing The Last Character Is : ",removing_last_character_from_sentence)
    removing_frist_last_character_from_sentence = sen[1:-1]
    print("The Sentence After Removing The Frist Character , And Last Character Is : ",removing_frist_last_character_from_sentence)
get_sentence(sentence)