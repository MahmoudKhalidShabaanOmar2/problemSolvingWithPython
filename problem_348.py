# write a python program to get sentence from the user , and then print the frist character , and last character from the sentence By Using Function Method =>
# sentence = input("Please Enter The Sentence Is : ")
# def get_sentence(sen) :
#     print("The Sentence Is : ",sen)
#     frist_character_from_sentence = sen[0]
#     print("The Frist Character From The Sentence Is : ",frist_character_from_sentence)
#     last_character_from_sentence = sen[-1]
#     print("The Last Character From The Sentence Is : ",last_character_from_sentence)
# get_sentence(sentence)

def get_sentence(sen) :
    frist_character_from_sentence = sen[0]
    last_character_from_sentence = sen[-1]
    return("The Sentence Is : "+sen+" , The Frist Character From The Sentence Is : "+frist_character_from_sentence+" , And The Last Character From The Sentence Is : "+last_character_from_sentence)
sentence = input("Please Enter The Sentence Is : ")
displaying_sentence = get_sentence(sentence)
print(displaying_sentence)