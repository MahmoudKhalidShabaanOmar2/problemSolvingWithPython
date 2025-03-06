# write a python program to get memory into giga bytes , and then converted to bytes by using different functions methods =>
# memory_into_giga_bytes = float(input("please enter the size of the memory into giga bytes is = "))
# def get_memory_into_bytes(memory_into_GB) :
#     print("the size of the memory into giga bytes is = "+str(memory_into_GB)+" giga bytes")
#     memory_into_bytes = memory_into_GB * 1073741824
#     print("the size of the memory into bytes is = "+str(memory_into_bytes)+" bytes")
# get_memory_into_bytes(memory_into_giga_bytes)

# def get_memory_into_bytes(memory_into_GB) :
#     print("the size of the memory into giga bytes is = "+str(memory_into_GB)+" giga bytes")
#     memory_into_bytes = memory_into_GB * 1073741824 
#     return("the memory into bytes is = "+str(memory_into_bytes)+" bytes")
# memory_into_giga_bytes = float(input("please enter the size of the memory into giga bytes is = "))
# bytes = get_memory_into_bytes(memory_into_giga_bytes)
# print(bytes)

# memory_into_giga_bytes = float(input("please enter the size of the memory into giga bytes is = "))
# def get_memory_into_bytes(memory_into_GB) :
#     print("the size of the memory into giga bytes is = "+str(memory_into_GB)+" giga bytes")
#     if(memory_into_GB > 0) :
#         memory_into_bytes = memory_into_GB * 1073741824
#         print("the size of the memory into bytes is = "+str(memory_into_bytes)+" bytes , because your entered memory into giga bytes is = "+str(memory_into_GB)+" giga bytes")
#     else :
#         print("there is no size of the memory into bytes , because your entered memory into giga bytes is = "+str(memory_into_GB)+" giga bytes")
# get_memory_into_bytes(memory_into_giga_bytes)

def get_memory_into_bytes(memory_into_GB) :
    print("the size of the memory into giga bytes is = "+str(memory_into_GB)+" giga bytes")
    if(memory_into_GB > 0) :
        memory_into_bytes = memory_into_GB * 1073741824
        return("the size of the memory into bytes is = "+str(memory_into_bytes)+" bytes , beccause your entered size of memory into giga bytes is = "+str(memory_into_GB)+" giga bytes")
    else :
        return("there is no size of the memory into bytes , because your entered size of the memory into giga bytes is = "+str(memory_into_GB)+" giga bytes")
memory_into_giga_bytes = float(input("please enter the size of the memory into giga bytes is = "))
bytes = get_memory_into_bytes(memory_into_giga_bytes)
print(bytes)