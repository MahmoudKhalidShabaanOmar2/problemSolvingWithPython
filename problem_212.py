# write a python program to get size of the memory into bytes , and then  converted to giga bytes by using different functions methods => 
# memory_into_bytes = int(input("please enter the size of the memory into bytes is = "))
# def get_memory_into_giga_bytes(memory_into_B) :
#     print("the size of the memory into bytes is = "+str(memory_into_B)+" bytes")
#     memory_into_giga_bytes = memory_into_B / 1073741824 
#     print("the size of the memory into giga bytes is = "+str(memory_into_giga_bytes)+" giga bytes")
# get_memory_into_giga_bytes(memory_into_bytes)

# def get_memory_into_giga_bytes(memory_into_B) :
#     print("the size of the memory into bytes is = "+str(memory_into_B)+" bytes")
#     memory_into_giga_bytes = memory_into_B / 1073741824 
#     return("the size of the memory into giga bytes is = "+str(memory_into_giga_bytes)+" giga bytes")
# memory_into_bytes = int(input("please enter the size of the memory into bytes is = "))    
# giga_bytes = get_memory_into_giga_bytes(memory_into_bytes)
# print(giga_bytes)

# memory_into_bytes = int(input("please enter the size of the memory into bytes is = "))
# def get_memory_into_giga_bytes(memory_into_B) :
#     print("the size of the memory into bytes is = "+str(memory_into_B)+" bytes")
#     if(memory_into_B > 0) :
#         memory_into_giga_bytes = memory_into_B / 1073741824
#         print("the size of the memory into giga bytes is = "+str(memory_into_giga_bytes)+" giga bytes , because your entered size of the memory into bytes is = "+str(memory_into_B)+" bytes")
#     else :
#         print("there is no size of the memory into giga bytes , because your entered size of the memory into bytes is = "+str(memory_into_B)+" bytes")
# get_memory_into_giga_bytes(memory_into_bytes)

def get_memory_into_giga_bytes(memory_into_B) :
    print("the size of the memory into bytes is = "+str(memory_into_B)+" bytes")
    if(memory_into_B > 0) :
        memory_into_giga_byte = memory_into_B / 1073741824 
        return("the size of the memory into giga bytes is = "+str(memory_into_giga_byte)+" giga bytes , because your entered size of the memory into bytes is = "+str(memory_into_B)+" bytes")
    else :
        return("there is no size of the memory into giga bytes , because your entered size of the memory into bytes is = "+str(memory_into_B)+" bytes")
memory_into_bytes = int(input("please enter the size of the memory into bytes is = "))
giga_bytes = get_memory_into_giga_bytes(memory_into_bytes)
print(giga_bytes)