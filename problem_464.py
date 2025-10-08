# write a python program to get the user string sentence , and then get the reversing of the user substring sentence by using function method =>
user_string_sentence = input("Please Enter The User String Sentence Is : ") 
def get_reversing_sub_string(u_string):
    print("The User String Sentence Is : ",u_string)
    starting_number = int(input("Please Enter The Starting Number Is = "))
    print("The Starting Number Is = ",str(starting_number))
    ending_number = int(input("Please Enter The Ending Number Is = "))
    print("The Ending Number Is = ",str(ending_number))
    sub_string_sentence = u_string[starting_number:ending_number]
    print("The User Sub String Sentence Is : ",str(sub_string_sentence))
    reversing_sub_string_sentence = sub_string_sentence[::-1]
    print("The Reversing Of The User Sub String Sentence Is : ",reversing_sub_string_sentence)
get_reversing_sub_string(user_string_sentence) 