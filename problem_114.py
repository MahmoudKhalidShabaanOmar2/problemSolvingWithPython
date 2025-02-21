# write a python program to get sentence from the user , and then converted sentence into uppercase sentence by using different functions methods =>
# sentence = input("please enter the sentence is : ")
# def get_upper_sentence(sente) :
#     print("the sentence is : \'"+sente+"\'")
#     upper_sentence = sente . upper()
#     print("the upper sentence is : \'"+upper_sentence+"\'")
# get_upper_sentence(sentence)

def get_upper_sentence(sente) :
    print("the sentence is : \'"+sente+"\'")
    upper_sentence = sente . upper()
    return("the upper sentence is : \'"+upper_sentence+"\'")
sentence = input("please enter the sentence is : ")
upper_sent = get_upper_sentence(sentence)
print(upper_sent)