def max_in_list(mylist_str):
    mylist_int = [int(num) for num in mylist_str.split(',')]
    return max(mylist_int)

# mylist=[1,4,5,6,7,5]
mylist_str=input("Enter list of numbers:")
print(max_in_list(mylist_str))

