# write a python program to get sentence from the user , and get the reversing sentence , and display for the user between double qoutation , and at the end put full stop =>
sentence = input("please enter the sentence is : ")
print("the sentence is : \""+sentence+"\".")
reversing_sentence = ""
for i in sentence :
    reversing_sentence = i + reversing_sentence 
    print("\""+i+"\"")
print("the reversing sentence is : \""+reversing_sentence+"\"")
for j in reversing_sentence :
    print("\""+j+"\".")