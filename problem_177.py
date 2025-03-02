# write a python program to get sentence from the user , and then reverse the sentence , and display the result =>
sentence = input("please enter the sentence is : ")
print("the sentence is : "+sentence)
for i in sentence :
    print(i)
reversing_sentence = ""
print("the reversing senteence is : ")
for j in sentence :
    reversing_sentence = j + reversing_sentence 
print("the reversing sentence is : "+reversing_sentence)
for k in reversing_sentence :
    print(k)