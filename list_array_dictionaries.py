
# import array as ar
# my_game_scores = ar.array("d",[2.0,5,7,8])
# print (type(my_game_scores))
#
# my_set = {"one", "two", "bubkle", "My", "Shoe"}
#
# print (type(my_set))
# print(my_set)
#
# my_set.add("two")
# print(my_set)
#
# my_test_dictionary= {"first_name":"victor", "last_name":"granados"}
# print(my_test_dictionary)





# for with normal dictionary
my_dictionary = {"name":"Victor", "last_name":"Granados", "passport":"X675849" }

for key in my_dictionary:
    print(key)

# for with list nested in another list
nested_for_loop = [[1,2,3,4,],[5,6,7,8,]]

print(nested_for_loop[0][3])

for squares in nested_for_loop:
    print(squares)
    for squares2 in squares:
        print(squares2)
# for in a dictionary nested in another dictionary
my_dictiona = {"dictA": {"key_1": "value_1"},
                "dictB": {"key_2": "value_2"}}

for squares in my_dictiona.values():
    print(squares)
    for square_value in squares.values():
        print(square_value)





# list_of_values = [1,2,3,4,5,6,7,8,9]
#
# for item in list_of_values:
#     if item % 2 == 0:
#         #even numbers/numeros pares odd numbers/numeros impares
#         print(item)
#     elif item % 3 == 0:
#         print(item, "is multiple of 3 ")
#     else:
#         print("number is odd")









