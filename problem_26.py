#write a python program to get the difference between the two sets using function =>
# frist_set = {12 , 2 , 7 , 8 , 1 , 6}
# second_set = {15 , 0 , 1 , 3 , 6}
# def get_difference_set(fri_set , sec_set) :
#     print("the different values of the different sets is : \n")
#     print("the frist set is : "+str(fri_set))
#     print("the second set is : "+str(sec_set))
#     difference_set = fri_set . difference(sec_set)
#     print("the difference set between the two sets is : "+str(difference_set))
# get_difference_set(frist_set , second_set)

def get_difference_set(fri_set , sec_set) :
    print("the different values of the different sets is : \n")
    print("the frist set is : "+str(fri_set))
    print("the second set is : "+str(sec_set))
    difference_set = fri_set . difference(sec_set)
    return("the difference set between the two sets is : "+str(difference_set))
frist_set = {12 , 2 , 7 , 8 , 1 , 6}
second_set = {15 , 0 , 1 , 3 , 6}
diffErence = get_difference_set(frist_set , second_set)
print(diffErence)