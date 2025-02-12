# write a python program to get the symmetric difference between the two sets using function =>
# frist_set = {2 , 6 , 7 , 8 , 1 , 12}
# second_set = {1 , 3 , 15 , 6 , 0}
# def get_symmetric_difference_set(fri_set , sec_set) :
#     print("the different values of the different sets is : \n")
#     print("the frist set is : "+str(fri_set))
#     print("the second set is : "+str(sec_set))
#     symmetric_difference_set = fri_set . symmetric_difference(sec_set)
#     print("the symmetric difference set between the two difference sets is : "+str(symmetric_difference_set))
# get_symmetric_difference_set(frist_set , second_set)

def get_symmetric_difference_set(fri_set , sec_set) :
    print("the different values of the different two sets is : \n")
    print("the frist set is : "+str(fri_set))
    print("the second set is : "+str(sec_set))
    symmetric_difference_set = fri_set . symmetric_difference(sec_set)
    return("the symmetric difference between the two sets is : "+str(symmetric_difference_set))
frist_set = {2 , 6 , 7 , 8 , 1 , 12}
second_set = {1 , 3 , 15 , 6 , 0}
symmetricDifference = get_symmetric_difference_set(frist_set , second_set)
print(symmetricDifference)