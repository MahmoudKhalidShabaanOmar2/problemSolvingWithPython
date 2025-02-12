# write a python program to get the union of the two sets by using function methods => 
# frist_set = {2 , 3 , 4 , 5 , 6 , 7 , 8}
# second_set = {4 , 12 , 5 , 1 , 6 , 8}
# def get_union_set(fri_set , sec_set) :
#     print("the different values of the different sets is : \n")
#     print("the frist set is : "+str(fri_set))
#     print("the second set is : "+str(sec_set))
#     union_set = fri_set . union(sec_set)
#     print("the union of the two sets is : "+str(union_set))
# get_union_set(frist_set , second_set)

def get_union_set(fri_set , sec_set) :
    print("the different values of the different sets is : \n")
    print("the frist set is : "+str(fri_set))
    print("the second set is : "+str(sec_set))
    union_set = fri_set . union(sec_set)
    return("the union of the two sets is : "+str(union_set))
frist_set = {2 , 3 , 4 , 5 , 6 , 7 , 8}
second_set = {4 , 12 , 5 , 1 , 6 , 8}
unIon = get_union_set(frist_set , second_set)
print(unIon)