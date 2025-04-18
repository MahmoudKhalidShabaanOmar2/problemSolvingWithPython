# write a python program to print characters from a string that are present at an odd index number => 
sentence = input("Please Enter The Sentence Is : ")
print("The Sentence Is : "+sentence)
len_of_sentence = len(sentence)
print("The Length Of The Sentence Is = "+str(len_of_sentence)+" Characters")
for i in range(1 , len_of_sentence) :
    if(i %2 != 0) :
        print(sentence[i])
    else :
        print("It Is Even Index Character")