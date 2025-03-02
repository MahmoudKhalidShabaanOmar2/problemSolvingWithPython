# write a python program to get sentence from the user , and then get the reversing sentence of the sentence , and at the end get the reversing sentence between double qoutation , and at the end put full stop by using function methods =>
sentence = input("please enter the sentence is : ")
def get_reversing_sentence(sen) :
    print("the sentence is : \""+sen+"\".")
    reversing_sentence = ""
    for i in sen :
        reversing_sentence = i + reversing_sentence 
        print("\""+i+"\".")
    print("the reversing sentence is : \""+reversing_sentence+"\".")
    for j in reversing_sentence :
        print("\""+j+"\".")
get_reversing_sentence(sentence)