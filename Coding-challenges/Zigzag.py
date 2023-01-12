def zigzag(x):
    for i in range(x):
        if i % 2 == 0:
            print("* " * (x - i))
        else:
            print(" *" * (x - i))

    # Af the last iteration the value of i = 5

    for j in range(x+1):
        if j % 2 == 0:
            print("* " * (x - (x-j)))
        else:
            print(" *" * (x - (x-j)))
zigzag(6)

# def savas(y):
#     fixed = y
#     for i in range(y):
#         print("Step ",i+1,":", end=" ") # added step number
#         if i % 2 == 0:
#             for j in range(y - i):
#                 print("a l ", end="") # added end="" to prevent new line
#             print("") # added new line
#         else:
#             for j in range(y - i):
#                 print(" a l", end="") # added end="" to prevent new line
#             print("") # added new line
#     # Reverse the step numbers and zigzag
#     for i in range(fixed):
#         print("Step ",i+1,":", end=" ") # added step number
#         if i % 2 == 0:
#             for j in range(fixed + i):
#                 print("* ", end="") # added end="" to prevent new line
#             print("") # added new line
#         else:
#             for j in range(fixed + i):
#                 print(" *", end="") # added end="" to prevent new line
#             print("") # added new line
# savas(5)

# import math
# def zigzag_pattern(rows):
#     for i in range(1, rows + 1):
#         print("Step ",i,":", end=" ")
#         if i <= math.floor(rows/2):
#             print("a " * (rows - i + 1))
#         elif i == math.floor(rows/2) + 1:
#             print("* " * (rows - i + 1))
#         else:
#             for j in range(i - math.floor(rows/2) - 1):
#                 print("* ", end="")
#             for k in range(rows - i + 1):
#                 print("a ", end="")
#             print("")

# zigzag_pattern(5)