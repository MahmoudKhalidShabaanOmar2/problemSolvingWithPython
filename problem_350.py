# write a python program to get sentence from the user , to print character that a string present at odd index by using function method =>
sentence = input("Please Enter The Sentence Is : ")
def get_sentence(sen) :
    print("The Sentence Is : ",sen)
    length_of_sentence = len(sen)
    print("The Length Of The Sentence Is = ",str(length_of_sentence)," Characters")
    print("The Odd Index Characters Only From The Sentence Is : ")
    for j in range(0 , length_of_sentence) :
        if(j %2 != 0) :
            print(sen[j])
get_sentence(sentence)

# def get_sentence(sen) :
#     print("The Sentence Is : ",sen)
#     length_of_sentence = len(sen)
#     print("The Length Of The Sentence Is = ",str(length_of_sentence)," Characters")
#     print("The Odd Index Characters Only From The Sentence Is : ")
#     for j in range(0 , length_of_sentence) :
#         if(j %2 != 0) :
#             print(sen[j])
#     return("")
# sentence = input("Please Enter The Sentence Is : ")
# displaying_sentence = get_sentence(sentence)
# print(displaying_sentence)            