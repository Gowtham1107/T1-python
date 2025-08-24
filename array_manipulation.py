# def add(arr,x):
#     arr_modified = [int(x)+int(element) for element in arr.split(',')]
#     return(arr_modified)

# input_arr = input("Enter an array: ")
# step_to_add = input("Enter step to add to each element ")
# print(f"modified array is {add(input_arr, step_to_add)}")




def equal(arr,x):
    matching_list=[element for element in arr.split(',') if int(element) == int(x)]
    return(matching_list)

input_arr = input("Enter an array: ")
match_number = input("Enter element to match: ")
print(f"mached elemnts array is {equal(input_arr,match_number)}")

