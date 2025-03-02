# write a python program to get sentence from the user , and then get the reversing sentence , and display reversing sentence for the user by using different function method =>
sentence = input("please enter the sentence is : ")
def get_reversing_sentence(sen) :
    print("the sentence is : "+sen)
    reversing_sentence = ""
    for i in sen : 
        reversing_sentence = i + reversing_sentence 
        print(i)
    print("the revcersing sentence is : "+reversing_sentence)
    for j in reversing_sentence :
        print(j)
get_reversing_sentence(sentence) 