# write a python program to get sentence from the user to print character that are present at even index number =>
sentence = input("Please Enter The Sentence Is : ")
print("The Sentence Is : "+sentence)
len_of_sentence = len(sentence)
print("The Length Of The Sentence Is : "+str(len_of_sentence)+" Characters")
for i in range(0 , len_of_sentence) :
    if(i %2 == 0) :
        print(sentence[i])
    else :
        print("It Is Odd Index Character")