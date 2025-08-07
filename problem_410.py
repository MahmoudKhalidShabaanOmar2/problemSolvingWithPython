# write a python program to update the specific keys in the dictionary =>
my_dict = {
    "name": "Mahmoud",
    "age": 25,
    "country": "Egypt"
}
print("Original Dictionary:", my_dict)
key_to_update = input("Enter the key you want to update: ")
if key_to_update in my_dict:
    new_value = input(f"Enter the new value for '{key_to_update}': ")
    my_dict[key_to_update] = new_value
    print("Updated Dictionary:", my_dict)
else:
    print(f"Key '{key_to_update}' not found in the dictionary.")