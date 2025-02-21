# write a python program to get sentence from the user , and then get the capitalize of the sentence by using different function methods =>
# sentence = input("please enter the sentence is : ")
# capitalize_sentence = sentence . capitalize()
# def get_capitalize_sentence(sente , cap_sente) :
#     print("the sentence is : \""+sente+"\"")
#     print("the capitalize sentence is : \""+cap_sente+"\"")
# get_capitalize_sentence(sentence , capitalize_sentence)

def get_capitalize_sentence(sente , cap_sente) :
    print("the sentence is : \""+sente+"\"")
    return("the capitalize sentence is \""+cap_sente+"\"")
sentence = input("please enter the sentence is : ")
capitalize_sentence = sentence . capitalize()
capitalize_sen = get_capitalize_sentence(sentence , capitalize_sentence)
print(capitalize_sen)