# def lesser_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:
#         if a < b:
#             print(a)
#         else:
#             print(b)

#     elif a % 2 == 0 or b % 2 == 0:
#         if a > b:
#             print(a)
#         else:
#             print(b)

# lesser_of_two_evens(4, 2)


# def animal_crackers(text):
#     word = text.split()
#     if word[0][0].lower() == word[1][0].lower():
#       print(True)
#     else:
#       print(False)

# animal_crackers('Level llama')


# def other_side_of_seven(num):
#     if num < 7:
#         twice = (7 - num) * 2
#         print(twice + 7)
#     else:
#         twice = (num - 7) * 2
#         print(7 - twice)

# other_side_of_seven(12)


# def old_macdonald(name):
#   print(name[0].capitalize()+name[1:3]+name[3].capitalize()+name[4:])

# old_macdonald('macdonald')


# def master_yoda(text):
#     word = text.split()
#     new = " ".join(word[::-1])
#     print(new)

# master_yoda('I am home')


# def almost_there(n):
#     num100 = abs(100 - n)
#     num200 = abs(200 - n)
#     if (num100 <= 10 or num200 <= 10):
#         print(True)
#     else:
#         print(False)

# almost_there(190)


def paper_doll(text):
    print("".join([x*3 for x in text]))

paper_doll('Mississippi')


# def spy_game(*nums):
#     str_nums = str(nums)
#     if '0, 0, 7' in str_nums:
#         print(True)
#     else:
#         print(False)

# spy_game([1, 2, 4, 0, 9, 7, 5])