# marks = {}
# print(type(marks))

# marks['Maths'] = 80
# marks['Chemistry'] = 50
# marks['Social'] = 94.5
# marks[123] = 100

# print(f"type of marks is {type(marks['Social'])}")
# print(f"type of marks is {type(marks[123])}")

# print(marks)



# Can list be used as key?  Ans: NO
#Error     list_to_sum[arr] = 6
#     ~~~~~~~~~~~^^^^^
# TypeError: unhashable type: 'list'

# list_to_sum = {}

# arr = [1,2,3]

# list_to_sum[arr] = 6

# print(list_to_sum)

# NOTE: we can use list as value 


#we can use tuple a key


tup_to_sum = {}

tup = (1,2,3)

tup_to_sum[tup] = 6

print(tup_to_sum)